function checkBellTime() {
    if (!userLoggedIn) return;

    const now = new Date();
    const currentHour = now.getHours().toString().padStart(2, '0'); // Ensures 2-digit format
    const currentMinutes = now.getMinutes().toString().padStart(2, '0'); // Ensures 2-digit format
    const formattedTime = `${currentHour}:${currentMinutes}`;

    const dayOfWeek = now.getDay(); // 0 = Sunday, 1 = Monday, ..., 6 = Saturday
    const dateOfMonth = now.getDate(); // Gets day of the month (1-31)

    // 🔴 Disable ringing on Sundays & 1st/3rd Saturdays
    if (dayOfWeek === 0 || (dayOfWeek === 6 && (dateOfMonth <= 7 || (dateOfMonth >= 15 && dateOfMonth <= 21)))) {
        return; // Prevent ringing
    }

    // 🛎️ Bell Timings
    const normalBellTimes = ["09:00", "09:55", "10:50", "11:10", "12:05", "13:00", "13:55", "14:50", "15:00", "15:50", "16:40"];
    const examBellTimes = ["09:55", "10:00", "11:55", "12:00"];

    const isLastBell = formattedTime === "16:40" || formattedTime === "12:00";
    const bellDuration = isLastBell ? 10000 : 5000;

    // 🎵 Play Bell Sound Smoothly
    function playBell(audioId) {
        const audio = document.getElementById(audioId);
        if (audio) {
            audio.volume = 0.8;
            audio.play();
            setTimeout(() => {
                audio.pause();
                audio.currentTime = 0; // Reset for next ring
            }, bellDuration);
        }
    }

    // 🔔 Trigger Bell
    if (normalBellTimes.includes(formattedTime)) {
        playBell("normal-bell-audio");
    } else if (examBellTimes.includes(formattedTime)) {
        playBell("exam-bell-audio");
    }
}

// ⏰ Check Bell Time Every Minute
const userLoggedIn = true; // This will be dynamically set when a user logs in
setInterval(checkBellTime, 60000);