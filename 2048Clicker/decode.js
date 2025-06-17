document.getElementById("process").addEventListener("click", function(event) {
    event.preventDefault();

    let saveDataInput = document.getElementById("savedata").value;
    let decodedData = atob(saveDataInput); // Decode Base64

    try {
        let formattedData = JSON.stringify(JSON.parse(decodedData), null, 2);
        document.getElementById("decoded").value = formattedData;
    } catch (error) {
        document.getElementById("decoded").value = "Invalid JSON format. Unable to process save data.";
        console.error("Error parsing JSON:", error);
    }
});
