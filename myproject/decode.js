document.getElementById("process").addEventListener("click", function(event) {
    event.preventDefault();

    // Get the user input from the save data text area
    let saveDataInput = document.getElementById("savedata").value;

    // Decode the save data (assuming Base64 encoding)
    let decodedData = atob(saveDataInput);

    // Store the decoded data instead of printing
    let rawDecodedData = decodedData;
    let formattedData = JSON.stringify(JSON.parse(decodedData), null, 2);

    // Display the decoded data in the output textarea
    document.getElementById("decoded").value = formattedData;
});
