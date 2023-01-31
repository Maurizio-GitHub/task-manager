// Templating languages such as Flask require any internal assets to be stored in a directory called 'static'

document.addEventListener("DOMContentLoaded", function() {
    // Sidenav initialization:
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);

    // Datepicker initialization:
    let datepicker = document.querySelectorAll(".datepicker");
    M.Datepicker.init(datepicker, {
        format: "dd mmmm, yyyy",
        i18n: {done: "Select"}
    });

    // Select initialization:
    let selects = document.querySelectorAll("select");
    M.FormSelect.init(selects);

    // Collapsible initializataion:
    let collapsibles = document.querySelectorAll(".collapsible");
    M.Collapsible.init(collapsibles);
});