showTime()
setInterval(showTime, 1000)

function showTime() {
    let dt = new Date()

    let h = dt.getHours()
    let m = dt.getMinutes()
    let s = dt.getSeconds()

    let hours = document.querySelector("#hours")
    let minutes = document.querySelector("#minutes")
    let seconds = document.querySelector("#seconds")

    hours.textContent = h
    minutes.textContent = m
    seconds.textContent = s

}