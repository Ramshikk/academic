function checkingjj()
{
	alert('ggggg');
		var chk1 = document.getElementById('chk1');
        var dependentCheckboxes = document.querySelectorAll('.dependentCheckbox');

        
            dependentCheckboxes.forEach(function (checkbox) {
                checkbox.checked = chk1.checked;
             });
        
}
function divdisplay()
{
    $(document).ready(function() {
    // Change the select element ID to match yours
    var selectElement = $("#empcatg");

    // Disable the select element initially if needed
    // selectElement.prop('disabled', true);

    // Add change event listener to the select element
    selectElement.change(function() {
        // Get the selected value
        var selectedValue = $(this).val();

        // Define the condition for disabling the select element
        var condition = (selectedValue == "{{ settings.EMP_CAT_AREA_ACCOUNTANT }}");

        // Apply the condition to disable or enable the select element
        selectElement.prop('disabled', condition);
    });
});
}
