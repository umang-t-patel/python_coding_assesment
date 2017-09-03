var loadForm = function () {
    /*
    This function loads the form in order to create appointment.
    It has two functionality:
      1. Loads form:
          It renames the 'New' button to 'Add' then shows create form panel.
      2. Saves form:
          If user fills the appropriate Date, Time and Description and click Add.
          It saves the filled information and renames the 'Add' button to 'New' then hides create form panel.
    */
    var btn = $(this);
    // If button is not add then load the create form
    if (btn.text() !== "Add") {
        btn.text("Add");
        // Show cancel button
        $(".js-cancel-appointment").show(400);
        // Ajax call to load the partial_appointment_list.html
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                // Reset the container before send
                $(".js-create-body").html("");
                // Show panel to populate it with partial_appointment_list.html contents
                $(".js-create-panel").show(400);
            },
            success: function (data) {
                //Load partial_appointment_list.html
                $(".js-create-body").html(data.html_form);
            }
        });
    }
    else {
        // If button is add then load the create form
        var form = $("#appointment_form");
        // Ajax call to save form and retrieve all data with newly added data
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                    // Show updated list of data
                    $(".js-list-body").html(data.html_appointment_list);
                    // Rename 'add' to 'new'
                    $(".js-create-appointment").text("New");
                    // Hide cancel button
                    $(".js-cancel-appointment").hide(400);
                    $(".js-create-body").html("");
                    // Hide create panel
                    $(".js-create-panel").hide(400);
                    $("#search_input").val('');
                }
                else {
                    $(".js-create-body").html(data.html_form);
                }
            }
        });
        return false;
    }
};
var cancelForm = function () {
    /*
    This function unloads/hide the create appointment form.
        It renames the 'Add' button to 'New'
        It hides the cancel button
        It hides create appointment form panel
    */
    var btn = $(this);
    $(".js-create-appointment").text("New");
    $(".js-cancel-appointment").hide(400);
    $(".js-create-body").html("");
    $(".js-create-panel").hide(400);
};
var searchForm = function () {
    /*
    This function is called on onLoad and if user press search button
        1. No search text:
            This will retrieve all data from the table when dom loads
            or
            when user click search in which the search text box is empty
        2. Search Text:
            This will retrieve the selective rows which contains the search text in appointment description column .
    */
    var form = $("#appointment_search");
    // Get the value from the search text box
    var search = $("#search_input").val();
    $.ajax({
        url: form.attr("action"),
        data: {'csrfmiddlewaretoken': csrftoken, 'search_text': search},
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
            // Show list of data with filter or without filter when text is blank
            $(".js-list-body").html(data.html_appointment_list);
        }
    });
    return false;
};
$(document).ready(function () {
    // Hide cancel button on dom load.
    $(".js-cancel-appointment").hide();
    // Hide create panel on dom load.
    $(".js-create-panel").hide();
    // Call searchForm function at dom load to load all existing appointment.
    searchForm();
    // Bind the loadForm function to create appointment button.
    $(".js-create-appointment").click(loadForm);
    // Bind the cancelForm function to cancel appointment button.
    $(".js-cancel-appointment").click(cancelForm);
    // Bind the searchForm function to search appointment button.
    $(".js-search-appointment").click(searchForm);
});
