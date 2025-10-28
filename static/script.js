const events = [
  {
    name: "Tech Symposium",
    date: "2025-07-10",
    time: "10:00 AM",
    venue: "Auditorium",
    brochureImage: "img1.jpeg",
    register: "https://forms.gle/exampleForm1"
  },
  {
    name: "Cultural Fest",
    date: "2025-07-15",
    time: "6:00 PM",
    venue: "Open Ground",
    brochureImage: "img2.jpeg",
    register: "https://forms.gle/exampleForm2"
  }
];

const eventList = document.getElementById("event-list");

events.forEach(event => {
  const div = document.createElement("div");
  div.className = "event-card";
  div.innerHTML = `
    <img src="${event.brochureImage}" alt="Event Brochure" class="brochure-img" />
    <h3>${event.name}</h3>
    <p><strong>📅 Date:</strong> ${event.date}</p>
    <p><strong>🕒 Time:</strong> ${event.time}</p>
    <p><strong>📍 Venue:</strong> ${event.venue}</p>
    <a href="${event.register}" target="_blank" class="register-btn">Register Now</a>
  `;
  eventList.appendChild(div);
});

