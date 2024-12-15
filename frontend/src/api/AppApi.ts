import axios from 'axios'

const baseURL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:3010'

// GitHub Actions の動作確認用のコミットのためのコメント

export const AppApi = axios.create({
  // vite.config.ts で server.proxy を定義しても反映されないのでここで URL 定義する
  baseURL,
  responseType: 'json',
  headers: {
    'Content-Type': 'application/json',
  },
})
