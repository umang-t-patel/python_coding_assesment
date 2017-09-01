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
  if (btn.text() !== "Add") {
    btn.text("Add");
    $(".js-cancel-appointment").show(400);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $(".js-create-body").html("");
        $(".js-create-panel").show(400);
      },
      success: function (data) {
        $(".js-create-body").html(data.html_form);
      }
    });
  }
  else {
    var form = $("#appointment_form");
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $(".js-list-body").html(data.html_appointment_list);
          $(".js-create-body").html("");
          $(".js-create-panel").hide(400);
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
  var btn = $(this);
  $(".js-create-appointment").text("New");
  $(".js-cancel-appointment").hide(400);
  $(".js-create-body").html("");
  $(".js-create-panel").hide(400);
};
var searchForm = function () {
  var form = $("#appointment_search");
  var search = $("#search_input").val();
  $.ajax({
    url: form.attr("action"),
    data: { 'csrfmiddlewaretoken':csrftoken,'search_text' : search},
    type: form.attr("method"),
    dataType: 'json',
    success: function (data) {
      $(".js-list-body").html(data.html_appointment_list);
    }
  });
  return false;
};
$(document).ready(function() {
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
