# photo-library

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

## Installation

リポジトリをクローンした後、以下のコマンドを実行して管理者ユーザーを作成してください。

```shell-session
$ cd backend
$ pipenv run ./manage.py migrate
$ pipenv run ./manage.py createsuperuser  # Create an admin user
ユーザー名: yk-lab
メールアドレス: yk-lab@users.noreply.github.com
表示名: yk-lab
Password:
Password (again):
Superuser created successfully.
```

## Configuration

### Environment Variables (環境変数)

環境変数や `.env` ファイルを使用して設定を行います。

| Name | Description | Required | Default |
| ---- | ----------- | -------- | ------- |
| SECRET_KEY | Django secret key | Yes | |
| SECRET_KEY_FALLBACKS | Fallback secret keys | No | |
| ALLOWED_HOSTS | Allowed hosts. Comma-separated list. | Yes | |
| ENVIRONMENT | Environment name | No | `Local` |
| FORCE_HTTPS | Force HTTPS | No | If `ENVIRONMENT` is `Local`, `False`. Otherwise, `True`. |
| DEBUG | Debug mode | No | `False` |
| SENTRY_DSN | [Sentry](https://sentry.io/) DSN | No | |
| SENTRY_TRACES_SAMPLE_RATE | Sentry traces sample rate | No | `0.0` |
| SENTRY_PROFILES_SAMPLE_RATE | Sentry profiles sample rate | No | `0.0` |

### Application Settings (アプリケーション設定)

管理者ユーザでログインすることで、以下の設定を行うことができます。

#### Account (アカウント)

| Name | Description | Default |
| ---- | ----------- | ------- |
| ACCOUNT_IS_OPEN_FOR_SIGNUP | 自己サインアップを許可するかどうか | `False` |

## For Contributors

### Prerequisites

- Pipenv

### Setup

リポジトリをクローンした後、以下のコマンドを実行してください。

```shell-session
$ pipenv sync --dev  # Install dependencies for development
$ pipenv run pre-commit install  # Install pre-commit hooks
Loading .env environment variables...
pre-commit installed at .git/hooks/pre-commit
```
