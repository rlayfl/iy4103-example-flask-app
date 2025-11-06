function getFormInputFieldsContent() {
    
    var phoneNumber = document.getElementById("inputPhone").value;

    alert("Your phone number is : " + phoneNumber)

    if (length(phoneNumber) < 10) {
        alert("Please enter a valid phone number");
        return false;
    }

}