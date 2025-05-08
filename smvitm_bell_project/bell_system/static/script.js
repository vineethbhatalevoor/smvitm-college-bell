function checkBellTime() {
    if (!userLoggedIn) return;

    const now = new Date();
    const currentHour = now.getHours();
    const currentMinutes = now.getMinutes();
    const formattedTime = `${currentHour}:${currentMinutes}`;

    const dayOfWeek = now.getDay(); // 0 = Sunday, 1 = Monday, ..., 6 = Saturday
    const dateOfMonth = now.getDate(); // Gets day of the month (1-31)

    // Disable ringing on Sundays (dayOfWeek === 0) and 1st/3rd Saturdays
    if (dayOfWeek === 0 || (dayOfWeek === 6 && (dateOfMonth <= 7 || (dateOfMonth >= 15 && dateOfMonth <= 21)))) {
        return; // Do nothing, prevent ringing
    }

    // Normal scheduled bell timings
    const normalBellTimes = ["9:00", "9:55", "10:50", "11:10", "12:05", "13:00", "13:55", "14:50", "15:00", "15:50", "16:40"];
    const examBellTimes = ["9:55", "10:00", "11:55", "12:00"];

    const isLastBell = formattedTime === "16:40" || formattedTime === "12:00";
    const bellDuration = isLastBell ? 10000 : 5000;

    if (normalBellTimes.includes(formattedTime)) {
        const audio = document.getElementById("normal-bell-audio");
        audio.play();
        setTimeout(() => audio.pause(), bellDuration);
    } else if (examBellTimes.includes(formattedTime)) {
        const audio = document.getElementById("exam-bell-audio");
        audio.play();
        setTimeout(() => audio.pause(), bellDuration);
    }
}

// Check every minute
const userLoggedIn = true; // This will be dynamically set when a user logs in
setInterval(checkBellTime, 60000);