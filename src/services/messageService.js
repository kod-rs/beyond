import api from '@/services/api'

export default {
  fetchMessages() {
    return api.get(`messages/`)
              .then(response => response.data)
  },
  postMessage(payload) {
    return api.post(`messages/`, payload)
              .then(response => response.data)
  },
  deleteMessage(msgId) {
    return api.delete(`messages/${msgId}`)
              .then(response => response.data)
  },
  postLogin(username, password) {
    return api.post(`login/?username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`)
    .then(response => response.data)
  },
  customFunction() {
    return "hello";
  }
}