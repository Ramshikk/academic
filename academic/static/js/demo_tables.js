function delete_row(row){
        
    var box = $("#notifydele");
    box.addClass("open");
    
    box.find(".mb-control-yes").on("click",function(){
        box.removeClass("open");
        $("#"+row).hide("slow",function(){
            $(this).remove();
        });
    });
    
}


   /*function notyConfirm(){
        
        noty({
           
            text: 'Do you want to continue?',
            layout: 'topRight',
            buttons: [
                    {addClass: 'btn btn-success btn-clean', text: 'Ok', onClick: function($noty) {
                        $noty.close();
                        noty({text: 'You clicked "Ok" button', layout: 'topRight', type: 'success'});
                    }
                    },
                    {addClass: 'btn btn-danger btn-clean', text: 'Cancel', onClick: function($noty) {
                        $noty.close();
                        noty({text: 'You clicked "Cancel" button', layout: 'topRight', type: 'error'});
                        }
                    }
                ]
        })         }*/


      

       
    function notyConfirm(depid) {
       
        var box = $("#notifydele");
        box.addClass("open");
        var row = 'trid' + depid;
       
                
                noty({
                    text: 'Do you want to  continue?',
                    layout: 'topRight',
                    buttons: [
                        {
                            addClass: 'btn btn-success btn-clean mb-control-ok',
                            text: 'Ok',
                            onClick: function ($noty) {
                                $noty.close();
                                box.removeClass("open");
                                $("#" + row).hide("slow", function () {
                                    $(this).remove();
                                });
                                $.ajax({
                                    type: "GET",
                                    url: document.getElementById("txtdelpath").value,
                                    data: {
                                        'id': depid,
                                         
                                    },
                                    dataType: "json",
                                    success: function (data) {
                                noty({ text: 'Deleted successfully', layout: 'topRight', type: 'success',timeout:1000 });
                            },
                            error: function (error) {
                                console.log('Ajax request failed');
                                console.log(error);
                            }
                        });
                        }
                        },
                        {
                            addClass: 'btn btn-danger btn-clean mb-control-cancel',
                            text: 'Cancel',
                            onClick: function ($noty) {
                                $noty.close();
                                box.removeClass("open");
                                noty({ text: 'Deletion not possible', layout: 'topRight', type: 'error',timeout:1000 });
                            }
                        }
                    ]
                });
    
            
           
    }
    
    
    function  department_edit(depid){
       document.getElementById('spinner'+depid).className="fa fa_spinner"
       document.getElementById("txtedit").value=depid
        $.ajax({
            
            type:"GET",
            url:document.getElementById("txthost").value,
            data: {
                'id': depid
            },
            dataType: "json",
            success: function (data){
                
                document.getElementById("edeptname").value=data.deptname;
                document.getElementById("edeptcode").value=data.deptcode;
                document.getElementById('sts').value=(data.status);
                $("#modal_basic").modal('show');
                document.getElementById('spinner'+depid).className="fa fa-pencil-square-o"
             },
             error:function (error){
            console.log(error);
                }
            });
      
    }
   
     function departmentEditing() {
        
        var box = $("#notifydele");
        box.addClass("open");
    
        var did = $('#txtedit').val();
        var depName = $('#edeptname').val();
        var depCode = $('#edeptcode').val();
        var depStatus = $('#sts').val();
    
        noty({
            text: 'Do you want to continue to update department details?',
            layout: 'topRight',
            buttons: [
                {
                    addClass: 'btn btn-success btn-clean mb-control-ok',
                    text: 'Ok',
                    onClick: function ($noty) {
                        updateDepartment(did, depName, depCode, depStatus);
                        $noty.close();
                        box.removeClass("open");
                    }
                },
                {
                    addClass: 'btn btn-danger btn-clean mb-control-cancel',
                    text: 'Cancel',
                    onClick: function ($noty) {
                        $noty.close();
                        box.removeClass("open");
                        noty({ text: 'Department not updated', layout: 'topRight', type: 'error', timeout: 1000 });
                        $("#modal_basic").modal('hide');
                    }
                }
            ]
        });
    }
    //for updating the department detail while showing a popup do you want to delete
    function updateDepartment(id, depName, depCode, depStatus) {
        $.ajax({
            url: $('#txtpath').val(),
            data: {
                'id': id,
                'depname': depName,
                'depcode': depCode,
                'status': depStatus
            },
            dataType: "json",
            success: function (data) {
                // alert(data.message)
                handleUpdateSuccess(data.message);
            },
            error: function (error) {
                console.log(error);
                handleUpdateError(error);
            }
        });
    }
    
    function handleUpdateSuccess(message) {
        noty({ text: message, layout: 'topRight', type: 'success'});
       
        setTimeout(function() {
            $("#modal_basic").modal('hide');
            window.location.reload(true);
        }, 2000);
    }
    
    function handleUpdateError(error) {
        noty({ text: error, layout: 'topRight', type: 'error', timeout: 1000 });
        $("#modal_basic").modal('hide');
    }

    function editDesignation(depid)
    {
        document.getElementById('spinner'+depid).className="fa fa_spinner"
        document.getElementById("txtedit").value=depid
        $.ajax({
            
            type:"GET",
            url:document.getElementById("txthost").value,
            data: {
                'id': depid
            },
            dataType: "json",
            success: function (data){
                
                document.getElementById("editDname").value=data.desname;
                document.getElementById("editDcode").value=data.descode;
                document.getElementById('sts').value=(data.status);
                $("#modal_basic").modal('show');
                document.getElementById('spinner'+depid).className="fa fa-pencil-square-o"
             },
             error:function (error){
            console.log(error);
                }
            });
    }
    function designationEditing() {
        
        var box = $("#notifydele");
        box.addClass("open");
    
        var did = $('#txtedit').val();
        var desName = $('#editDname').val();
        var desCode = $('#editDcode').val();
        var deStatus = $('#sts').val();
    
        noty({
            text: 'Do you want to continue to update desigantion details?',
            layout: 'topRight',
            buttons: [
                {
                    addClass: 'btn btn-success btn-clean mb-control-ok',
                    text: 'Ok',
                    onClick: function ($noty) {
                        updateDesignation(did, desName, desCode, deStatus);
                        $noty.close();
                        box.removeClass("open");
                    }
                },
                {
                    addClass: 'btn btn-danger btn-clean mb-control-cancel',
                    text: 'Cancel',
                    onClick: function ($noty) {
                        $noty.close();
                        box.removeClass("open");
                        noty({ text: 'Designation not updated', layout: 'topRight', type: 'error', timeout: 1000 });
                        $("#modal_basic").modal('hide');
                    }
                }
            ]
        });
    }
    //for updating the department detail while showing a popup do you want to delete
    function updateDesignation(id, desName, desCode, deStatus) {
        $.ajax({
            url: $('#txtpath').val(),
            data: {
                'id': id,
                'desname': desName,
                'descode': desCode,
                'status': deStatus
            },
            dataType: "json",
            success: function (data) {
                // alert(data.message)
                handleUpdateSuccess(data.message);
            },
            error: function (error) {
                console.log(error);
                handleUpdateError(error);
            }
        });
    }


    //division
    function  divisionedit(depid){
        document.getElementById('spinner'+depid).className="fa fa_spinner"
        document.getElementById("txtedit").value=depid
         $.ajax({
             
             type:"GET",
             url:document.getElementById("txthost").value,
             data: {
                 'id': depid
             },
             dataType: "json",
             success: function (data){
                 
                 document.getElementById("editDname").value=data.divname;
                 
                 document.getElementById('sts').value=(data.status);
                 $("#modal_basic").modal('show');
                 document.getElementById('spinner'+depid).className="fa fa-pencil-square-o"
              },
              error:function (error){
             console.log(error);
                 }
             });
       
     }

     function divisionEditing() {
        
        var box = $("#notifydele");
        box.addClass("open");
    
        var did = $('#txtedit').val();
        var divName = $('#editDname').val();
        var divStatus = $('#sts').val();
    
        noty({
            text: 'Do you want to continue to update division details?',
            layout: 'topRight',
            buttons: [
                {
                    addClass: 'btn btn-success btn-clean mb-control-ok',
                    text: 'Ok',
                    onClick: function ($noty) {
                        updateDivision(did, divName, divStatus);
                        $noty.close();
                        box.removeClass("open");
                    }
                },
                {
                    addClass: 'btn btn-danger btn-clean mb-control-cancel',
                    text: 'Cancel',
                    onClick: function ($noty) {
                        $noty.close();
                        box.removeClass("open");
                        noty({ text: 'Division not updated', layout: 'topRight', type: 'error', timeout: 1000 });
                        $("#modal_basic").modal('hide');
                    }
                }
            ]
        });
    }
    //for updating the department detail while showing a popup do you want to delete
    function updateDivision(id, divName, divStatus) {
        $.ajax({
            url: $('#txtpath').val(),
            data: {
                'id': id,
                'divname': divName,
                'status': divStatus
            },
            dataType: "json",
            success: function (data) {
                // alert(data.message)
                handleUpdateSuccess(data.message);
            },
            error: function (error) {
                console.log(error);
                handleUpdateError(error);
            }
        });
    }

    //class edit
    function classedit(depid){
        document.getElementById('spinner'+depid).className="fa fa_spinner"
        document.getElementById("txtedit").value=depid
         $.ajax({
             
             type:"GET",
             url:document.getElementById("txthost").value,
             data: {
                 'id': depid
             },
             dataType: "json",
             success: function (data){
                 
                 document.getElementById("editCname").value=data.clsname;
                 
                 document.getElementById('sts').value=(data.status);
                 $("#modal_basic").modal('show');
                 document.getElementById('spinner'+depid).className="fa fa-pencil-square-o"
              },
              error:function (error){
             console.log(error);
                 }
             });
       
     }
     
     function classEditing() {
        
        var box = $("#notifydele");
        box.addClass("open");
    
        var did = $('#txtedit').val();
        var clsName = $('#editCname').val();
        var clsStatus = $('#sts').val();
    
        noty({
            text: 'Do you want to continue to update class details?',
            layout: 'topRight',
            buttons: [
                {
                    addClass: 'btn btn-success btn-clean mb-control-ok',
                    text: 'Ok',
                    onClick: function ($noty) {
                        updateclass(did, clsName, clsStatus);
                        $noty.close();
                        box.removeClass("open");
                    }
                },
                {
                    addClass: 'btn btn-danger btn-clean mb-control-cancel',
                    text: 'Cancel',
                    onClick: function ($noty) {
                        $noty.close();
                        box.removeClass("open");
                        noty({ text: 'class not updated', layout: 'topRight', type: 'error', timeout: 1000 });
                        $("#modal_basic").modal('hide');
                    }
                }
            ]
        });
    }
  
    function updateclass(id, clsName, clsStatus) {
        $.ajax({
            url: $('#txtpath').val(),
            data: {
                'id': id,
                'clsname': clsName,
                'status': clsStatus
            },
            dataType: "json",
            success: function (data) {
                // alert(data.message)
                handleUpdateSuccess(data.message);
            },
            error: function (error) {
                console.log(error);
                handleUpdateError(error);
            }
        });
    }
    //qualification edit
    function  qualificationedit(depid){
        document.getElementById('spinner'+depid).className="fa fa_spinner"
        document.getElementById("txtedit").value=depid
         $.ajax({
             
             type:"GET",
             url:document.getElementById("txthost").value,
             data: {
                 'id': depid
             },
             dataType: "json",
             success: function (data){
                 
                 document.getElementById("editQname").value=data.qualname;
                 
                 document.getElementById('sts').value=(data.status);
                 $("#modal_basic").modal('show');
                 document.getElementById('spinner'+depid).className="fa fa-pencil-square-o"
              },
              error:function (error){
             console.log(error);
                 }
             });
       
     }
     function qualificationEditing() {
        
        var box = $("#notifydele");
        box.addClass("open");
    
        var did = $('#txtedit').val();
        var qualname = $('#editQname').val();
        var qualStatus = $('#sts').val();
    
        noty({
            text: 'Do you want to continue to update qualification details?',
            layout: 'topRight',
            buttons: [
                {
                    addClass: 'btn btn-success btn-clean mb-control-ok',
                    text: 'Ok',
                    onClick: function ($noty) {
                        updatequalification(did, qualname, qualStatus);
                        $noty.close();
                        box.removeClass("open");
                    }
                },
                {
                    addClass: 'btn btn-danger btn-clean mb-control-cancel',
                    text: 'Cancel',
                    onClick: function ($noty) {
                        $noty.close();
                        box.removeClass("open");
                        noty({ text: 'qualification not updated', layout: 'topRight', type: 'error', timeout: 2000 });
                        $("#modal_basic").modal('hide');
                    }
                }
            ]
        });
    }
  
    function updatequalification(id, qualname, qualStatus) {
        $.ajax({
            url: $('#txtpath').val(),
            data: {
                'id': id,
                'qualname': qualname,
                'status': qualStatus
            },
            dataType: "json",
            success: function (data) {
                // alert(data.message)
                handleUpdateSuccess(data.message);
            },
            error: function (error) {
                console.log(error);
                handleUpdateError(error);
            }
        });
    }
    function  employeedit(depid){
        //alert('ggg')
        document.getElementById('spinner'+depid).className="fa fa_spinner"
        document.getElementById("txtedit").value=depid
         $.ajax({
             
             type:"GET",
             url:document.getElementById("txthost").value,
             data: {
                 'id': depid
             },
             dataType: "json",
             success: function (data){
                 
                 document.getElementById("editEname").value=data.empname;
                 document.getElementById("area").value=data.emparea;
                 document.getElementById('sts').value=data.status;
                 $("#modal_basic").modal('show');
                 document.getElementById('spinner'+depid).className="fa fa-pencil-square-o"
              },
              error:function (error){
             console.log(error);
                 }
             });
       
     }
     function EmployeeEditing() {
        
        var box = $("#notifydele");
        box.addClass("open");
    
        var did = $('#txtedit').val();
        var empname = $('#editEname').val();
        var emparea=$('#area').val();
        var empStatus = $('#sts').val();
    
        noty({
            text: 'Do you want to continue to update Employee details?',
            layout: 'topRight',
            buttons: [
                {
                    addClass: 'btn btn-success btn-clean mb-control-ok',
                    text: 'Ok',
                    onClick: function ($noty) {
                        updateemployee(did, empname,emparea, empStatus);
                        $noty.close();
                        box.removeClass("open");
                    }
                },
                {
                    addClass: 'btn btn-danger btn-clean mb-control-cancel',
                    text: 'Cancel',
                    onClick: function ($noty) {
                        $noty.close();
                        box.removeClass("open");
                        noty({ text: 'employee not updated', layout: 'topRight', type: 'error', timeout: 2000 });
                        $("#modal_basic").modal('hide');
                    }
                }
            ]
        });
    }
  
    function updateemployee(id, empname, emparea,empStatus) {
        $.ajax({
            url: $('#txtpath').val(),
            data: {
                'id': id,
                'empname': empname,
                'emparea': emparea,
                'status': empStatus
            },
            dataType: "json",
            success: function (data) {
                // alert(data.message)
                handleUpdateSuccess(data.message);
            },
            error: function (error) {
                console.log(error);
                handleUpdateError(error);
            }
        });
    }
    function  subjectclassview(subid){
        //alert(subid)
        document.getElementById('spinner'+subid).className="fa fa_spinner"
      
         $.ajax({
             
             type:"GET",
             url:document.getElementById("txthost").value,
             data: {
                 'id': subid
             },
             dataType: "json",
             
             success: function (data){
                //alert(data.subjectname)
                //console.log(data)
                 
                document.getElementById("subitem").innerHTML="Subject Name"+data.subjectname;
                document.getElementById("status").innerHTML="Status"+data.subjectsts;
                var classListHTML = '<ul>';
                for (var i = 0; i < data.classnames.length; i++) {
                    classListHTML += '<li>' + data.classnames[i] + '</li>';
                 }
                classListHTML += '</ul>';
                 document.getElementById("clsitem").innerHTML=classListHTML;
                 
                 $("#modal_basic").modal('show');
                 document.getElementById('spinner'+subid).className="fa fa-eye"
              },
              error:function (error){
             console.log(error);
                 }
             });
       
     }
     function SubjectclassEditing() {
        
        var box = $("#notifydele");
        box.addClass("open");
    
        var did = $('#txtedit').val();
        var subname = $('#').val();
        var emparea=$('#area').val();
        var empStatus = $('#sts').val();
    
        noty({
            text: 'Do you want to continue to update Employee details?',
            layout: 'topRight',
            buttons: [
                {
                    addClass: 'btn btn-success btn-clean mb-control-ok',
                    text: 'Ok',
                    onClick: function ($noty) {
                        updateSubjectclass(did, empname,emparea, empStatus);
                        $noty.close();
                        box.removeClass("open");
                    }
                },
                {
                    addClass: 'btn btn-danger btn-clean mb-control-cancel',
                    text: 'Cancel',
                    onClick: function ($noty) {
                        $noty.close();
                        box.removeClass("open");
                        noty({ text: 'employee not updated', layout: 'topRight', type: 'error', timeout: 2000 });
                        $("#modal_basic").modal('hide');
                    }
                }
            ]
        });
    }
  
    function  updateSubjectclass(id, empname, emparea,empStatus) {
        $.ajax({
            url: $('#txtpath').val(),
            data: {
                'id': id,
                'empname': empname,
                'emparea': emparea,
                'status': empStatus
            },
            dataType: "json",
            success: function (data) {
                // alert(data.message)
                handleUpdateSuccess(data.message);
            },
            error: function (error) {
                console.log(error);
                handleUpdateError(error);
            }
        });
    }
function subjectclassEdit(subid)
{
    document.getElementById('spinner'+subid).className="fa fa_spinner"
    document.getElementById("txtedit").value=subid
     $.ajax({
         
         type:"GET",
         url:document.getElementById("txtedithost").value,
         data: {
             'id': subid
         },
         dataType: "json",
         success: function (data){
             
             document.getElementById("editsubject").value=data.subjectname;
             document.getElementById('sts').value=data.status;
            
             for (var i = 0; i < data.classnames.length; i++)
             {
                var className = data.classnames[i];
                //alert(className);
                var checkbox = document.getElementById('dependentCheckbox' + className);
                if (checkbox) {
                    checkbox.checked = true;
                }
            else
                checkbox.checked=false;
             }
                
             $("#modal_basicupdate").modal('show');
             document.getElementById('spinner'+depid).className="fa fa-pencil-square-o"
          },
          error:function (error){
         console.log(error);
             }
         });
 }
 function hidediv(empid)
 {
    //alert(empid);
    var teacherdata=$('#classdiv');
    const arr=empid.split('+')

    if(arr[1]==2)
        teacherdata.show();
    else
        teacherdata.hide();
 }
//select subject based on class
function sublisting(classid)
{
   
    $.ajax({
        url: $('#txtpath').val(),
        data: {
            'id':classid,
            
        },
        dataType: "json",
        success: function (data) {

            var subListHTML = '<select>';
            for (var i = 0; i < data.subjects.length; i++) {
                subListHTML += '<option value="' + data.subjects[i].id +'">' + data.subjects[i].subjectname + '</option>';
            }
            subListHTML += '</select>';
            document.getElementById("sublist").innerHTML = subListHTML;
        },
        error: function (error) {
            console.log(error);
            handleUpdateError(error);
        }
    });
}

function isItemAlreadyExists(table, checkClass, checkSubject, checkDivision) {
    for (var i = 0; i < table.rows.length; i++) {
        var existingRow = table.rows[i];
        var existingClass = existingRow.cells[1].getElementsByTagName("input")[0].value;
        var existingSubject = existingRow.cells[2].getElementsByTagName("input")[0].value;
        var existingDivision = existingRow.cells[3].getElementsByTagName("input")[0].value;

        if (existingClass === checkClass && existingSubject === checkSubject && existingDivision === checkDivision) {
            return true; // Item already exists
        }
    }

    return false; // Item doesn't exist
}

function deleteRow(row) {
    var table = document.getElementById("mytbl").getElementsByTagName('tbody')[0];
    var rowIndex = row.rowIndex;
    table.deleteRow(rowIndex - 1);
}

function addRow() {
    
    var newClass = document.getElementById("classlist").value;
    var newSubject = document.getElementById("sublist").value;
    var newDivision = document.getElementById("divlist").value;

    if ((document.getElementById('classlist').options.selectedIndex == 0)&&(document.getElementById('divlist').options.selectedIndex == 0))
     {
        alert('Please Select  class and division');
        //document.getElementById('lblmsg').innerHTML = "Please Select  class and division";
    } 
    else {
        document.getElementById('lblmsg').innerHTML = "";

        var table = document.getElementById("mytbl").getElementsByTagName('tbody')[0];

        // Check for duplicates before inserting the new row
        if (isItemAlreadyExists(table, newClass, newSubject, newDivision)) {
            alert("Item already exists in the table.");
            return;
        }

        // Creating a new row
        var newRow = table.insertRow(table.rows.length);

        var cell1 = newRow.insertCell(0);
        cell1.innerHTML = table.rows.length;

        // Cell 2: Class
        var cell2 = newRow.insertCell(1);
        var classListDropdown = document.getElementById("classlist");
        var selectedClassOption = classListDropdown.options[classListDropdown.selectedIndex];
        cell2.innerHTML = selectedClassOption.text;
        var textbox1 = document.createElement("input");
        textbox1.type = "text";
        textbox1.id = "txtclass";
        textbox1.name = "txtclass";
        textbox1.style.display = "none";
        textbox1.value = selectedClassOption.value;
        cell2.appendChild(textbox1);

        // Cell 3: Subject
        var cell3 = newRow.insertCell(2);
        var subject = document.getElementById("sublist");
        cell3.innerHTML = subject.options[subject.selectedIndex].text;
        var textbox2 = document.createElement("input");
        textbox2.type = "text";
        textbox2.id = "txtsubject";
        textbox2.name = "txtsubject";
        textbox2.style.display = "none";
        textbox2.value = subject.options[subject.selectedIndex].value;
        cell3.appendChild(textbox2);

        // Cell 4: Division
        var cell4 = newRow.insertCell(3);
        var division = document.getElementById("divlist");
        cell4.innerHTML = division.options[division.selectedIndex].text;
        var textbox3 = document.createElement("input");
        textbox3.type = "text";
        textbox3.id = "txtdivision";
        textbox3.name = "txtdivision";
        textbox3.style.display = "none";
        textbox3.value = division.options[division.selectedIndex].value;
        cell4.appendChild(textbox3);

        // Cell 5: Action
        var cell5 = newRow.insertCell(4);
        var button = document.createElement("button");
        button.innerHTML = '<span class="fa fa-times"></span>';
        button.className = "btn btn-primary btn-round";
        button.onclick = function() {
            deleteRow(newRow);
        };
        cell5.appendChild(button);
    }
}
