                    /*$(document).ready(function () {
                        $('textarea').change(function () {
                            $(this).val($(this).val().replace(/\n{3,}/g, "\r\n"));
                        });
                    });

                    function TextAreaValue() {
                        document.getElementById("myform").submit();
                        document.getElementById("myarea").defaultValue = "Hello Guys!";
                    }

                    function checking() {
                        var textBox =  $.trim( $('input[type=text]').val() )
                        if (textBox == "") {
                            $("#error").show('slow');
                        }
                    }*/

                    function executeCode() {
                        /*alert("I'm Javascript in jQuery!!");*/
                        document.getElementById("CodeArea").submit();
                    }

                    $(document).ready(function() {          
                    $('#execute').click(function() {
                        if (!$('#myarea').val()) {
                            alert('You need to write some code to proceed !!');                            
                        }
                        else {
                            /*alert('Else Working !!');*/
                            //executeCode();   
                            document.getElementById("filename").value = '';
                            $("#CodeArea").submit();
                        }
                    })
                    });

                    $(document).ready(function() {
                        $('#save').click(function() {
                          var value = document.getElementById('myarea').value;
                          if (value === '') {
                            alert('To create file, you need to write some code to save in it !!');                               
                          }
                          else {
                            $('#exampleModal').modal('show');                                                
                          }
                        })
                    });

                    $(document).ready(function() {
                        $('#filesave').click(function() {
                          var value = document.getElementById('myarea').value;
                          if (value === '') {
                            alert('To create new file, you need to write some code to in it !!');
                            //alert = function(){};
                          }                          
                        })
                    });

                    function copycode() {
                        document.getElementById("myarea").value = "{{ file.codefile.url }}";
                    }

                    /*$(document).on("click", function(e) {
                        if (e.target === document || e.target.tagName === "BODY" || e.target.tagName === "HTML") {
                            alert("Worked!!");
                        }
                    });*/   /*for getting blank clicks*/ 
                    
                    
                    //To reload window :-
                        //window.location.reload();

                    /*function rload() {
                        window.location.reload();
                    }*/











                    function openNav() {
                        document.getElementById("mySidenav").style.width = "250px";
                        document.getElementById("mainLogin").style.marginLeft = "250px";
                        document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
                      }
                      
                      function closeNav() {
                        document.getElementById("mySidenav").style.width = "0";
                        document.getElementById("mainLogin").style.marginLeft= "0";
                        document.body.style.backgroundColor = "white";
                      }
              
                      function openNavSignUp() {
                          document.getElementById("mySidenavSignUp").style.width = "250px";
                          document.getElementById("mainSignUp").style.marginRight = "250px";
                          document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
                        }
                        
                        function closeNavSignUp() {
                          document.getElementById("mySidenavSignUp").style.width = "0";
                          document.getElementById("mainSignUp").style.marginRight = "0";
                          document.body.style.backgroundColor = "white";
                        }
              
                        function authen_Upload() {              
                          {% if not user.is_authenticated  %}
                              alert("To Upload A File, You Need To Login First !!");
                          {% else %}
                              document.getElementById("myform").submit();   
                              /*var SelectedFile = document.getElementById("ChooseFile").value;   // to get the name of the file which is selected by the user to be uploaded.                 
                              var SelectedFile_Ext = SelectedFile.slice(-2);
                              alert(SelectedFile);            
                              alert(document.getElementById("lang").value);
                              alert(SelectedFile_Ext);
                              if( SelectedFile_Ext == 'va' ) {
                                  document.getElementById("lang").value = "Python";
                              }*/                                
                          {% endif %}
                        }                                        
                        
                        function login_refresh() {            
                          //document.getElementById('LoginForm').submit();                                              
                          setTimeout(function(){ location.href = "http://127.0.0.1:8080/"; }, 5000);
                        }
              
                        
              
                        function login_refresh2() {
                          document.getElementById('LoginForm').submit();                         
                          //$("#staticBackdrop2").modal();
                          //setTimeout(function(){ $("#staticBackdrop2").modal("show"); }, 300);                                                                                                
                        }  
                        
                          /*  Close alert "Fade-out" effect  */
                        setTimeout(function(){ $("#alert").fadeOut("slow"); }, 2500);           