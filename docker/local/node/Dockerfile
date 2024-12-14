# https://hub.docker.com/_/node/tags
FROM node:23.4

WORKDIR /frontend

# タイムゾーンを日本にする
ENV TZ=Asia/Tokyo
# ローカル開発用なので development に指定してライブラリたちのログ出力などを詳細にする
# https://nodejs.org/en/learn/getting-started/nodejs-the-difference-between-development-and-production
ENV NODE_ENV=development

EXPOSE 3000
