const ctx = document.getElementById("studentChart");

if (ctx) {
    new Chart(ctx, {
        type: "line",
        data: {
            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            datasets: [{
                label: "Students",
                data: [40, 60, 90, 120, 150, 200],
                borderWidth: 3
            }]
        }
    });
}

const pie = document.getElementById("attendanceChart");

if (pie) {
    new Chart(pie, {
        type: "doughnut",
        data: {
            labels: ["Present", "Absent"],
            datasets: [{
                data: [95, 5]
            }]
        }
    });
}