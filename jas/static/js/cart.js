function changeActive() {
    if (document.getElementById("id_self_delivery").checked == true) {

        document.getElementById("id_delivery_adress").value = "";
        document.getElementById("id_delivery_time").value = "";
        document.getElementById("id_delivery_adress").disabled = true;
        document.getElementById("id_delivery_time").disabled = true;
    } else {
        document.getElementById("id_delivery_adress").disabled = false;
        document.getElementById("id_delivery_time").disabled = false;
    }
}
window.onload = changeActive();
