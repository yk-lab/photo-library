import { sentryVitePlugin } from '@sentry/vite-plugin';
import { resolve } from 'path';
import { webpackStats } from 'rollup-plugin-webpack-stats';
import { defineConfig } from 'vite';

const sentryPlugin = () => {
  if (!process.env.SENTRY_AUTH_TOKEN || !process.env.SENTRY_ORG || !process.env.SENTRY_PROJECT || !process.env.SENTRY_RELEASE_FINALIZE) {
    return null;
  }

  return sentryVitePlugin({
    authToken: process.env.SENTRY_AUTH_TOKEN,
    org: process.env.SENTRY_ORG,
    project: process.env.SENTRY_PROJECT,
    telemetry: false,
    release: {
      finalize: !!process.env.SENTRY_RELEASE_FINALIZE,
      setCommits: {
        auto: true,
      },
    },
  });
};

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
    sourcemap: true,
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

  plugins: [
    // Output webpack-stats.json file
    // https://relative-ci.com/documentation/guides/bundle-stats/vite
    webpackStats(),

    // Sentry Vite plugin
    // Put the Sentry vite plugin after all other plugins
    sentryPlugin(),
  ],
});
