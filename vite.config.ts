import { resolve } from 'path';
import { defineConfig } from 'vite';

// https://vitejs.dev/config/
export default defineConfig({
  // 開発環境のmain.tsが置いてある場所
  root: resolve('./frontend/src'),

  // Djangoでの静的ファイル配信設定である STATIC_URL と同じになるよう設定
  base: '/static/',

  server: {
    host: 'localhost',
    port: 5173,
    open: false,
    watch: {
      usePolling: true,
      disableGlobbing: false,
    },
  },

  css: {
    devSourcemap: true,
  },

  resolve: {
    extensions: ['.js', '.ts', '.json'],
  },

  build: {
    // コンパイル後の出力先。DJANGO_VITE_ASSET_PATHと一致させる
    outDir: resolve('./frontend/dist'),
    assetsDir: '',
    manifest: 'manifest.json',
    emptyOutDir: true,
    target: 'es2017',
    rollupOptions: {
      input: {
        index: resolve('./frontend/src/entries/index.ts'),
      },
      output: {
        chunkFileNames: undefined,
      },
    },
  },
});
