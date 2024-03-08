import axios from "axios";

// const backend = 'http://154.8.158.40:1234'
const backend = 'http://8.141.5.141:1234'

export function generatePost(path: string, data?: object) {
    return axios.post(backend + path, data,
        {headers: {'Content-Type': 'application/x-www-form-urlencoded'}})
}

export function generatePostJson(path: string, data?: object) {
    return axios.post(backend + path, data,
        {headers: {'Content-Type': 'application/json'}})
}

export function getTime(){
    const val = new Date();
    const year = val.getFullYear()
    const month = (val.getMonth() + 1).toString().padStart(2, '0')
    const day = val.getDate().toString().padStart(2, '0')

    const hour = val.getHours().toString().padStart(2, '0')
    const mm = val.getMinutes().toString().padStart(2, '0')
    const ss = val.getSeconds().toString().padStart(2, '0')
    return year + "-" + month + "-" + day + " " + hour + ":" + mm + ":" + ss
}

// 00:00 - 08:59
export function isMorning() {
    return new Date().getHours() < 9
}