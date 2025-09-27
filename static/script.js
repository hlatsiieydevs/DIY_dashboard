async function updateDashboard() {
  try {
    const res = await fetch("/api/dashboard");
    const data = await res.json();

    document.getElementById("time").innerText = data.time;
    document.getElementById("date").innerText = data.date;

    document.getElementById("internet").innerText = data.internet ? "✅ Online" : "❌ Offline";

    if (!data.weather.error) {
      document.getElementById("temp").innerText = data.weather.temp + " °C";
      document.getElementById("wind").innerText = data.weather.wind_speed + " km/h";
      document.getElementById("sunrise").innerText = "🌅 " + data.weather.sunrise;
      document.getElementById("sunset").innerText = "🌇 " + data.weather.sunset;
    }

    const events = document.getElementById("events");
    events.innerHTML = "";
    data.calendar.forEach(e => {
      const li = document.createElement("li");
      li.textContent = `${e.time} - ${e.event}`;
      events.appendChild(li);
    });

  } catch (err) {
    console.error("Dashboard update failed:", err);
  }
}

// Update immediately + every 60s
setInterval(updateDashboard, 60000);
updateDashboard();
