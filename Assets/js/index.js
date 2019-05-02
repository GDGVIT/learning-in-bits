// // $(".sign").click(function(){
// //     $(".login").fadeToggle(300);
// //     setTimeout(function(){ 
// //         $(".signup").fadeToggle(300);
// //      }, 1000);
// // });
// let ob = {}
// let ob1 = {}
// let obt = {}
// let token
// // let token = Cookies.get("_ga");
// // console.log(token);

// $(document).ready(function () {
//     $(".b").click(function () {
//         ob.username = document.getElementById("name").value;
//         ob.password = document.getElementById("password").value;
//         //ob.token = token;
//         //console.log(ob)
//         console.log(JSON.stringify(ob))
//         console.log(document.cookie)

//         $.ajax({
//             url: 'https://stark-retreat-48003.herokuapp.com/login',
//             type: 'POST',
//             data: JSON.stringify(ob),
//             async: "true",
//             crossDomain: true,
//             crossOrigin: true,
//             dataType: 'json',
//             headers: {
//                 "accept": "application/json",
//                 "Access-Control-Allow-Origin": "*"
//             },
//             contentType: 'application/json',
//             success: function (response) {
//                 // let resp = JSON.parse(response)
//                 // console.log(resp.status);
//                 console.log(response)
//                 if (response.property === "success") {
//                     token = response.token
//                     alert(token)


//                     setTimeout(function () {
//                         profile(token)
//                         // window.location = "profile.html";
//                     }, 2000);

//                 } else {
//                     alert(response.property);
//                 }
//             },
//             error: function (err) {
//                 console.log("ERROR");
//                 console.log(err)
//             }
//         });

//     });

//     function profile(token) {
//         obt.token = token
//         alert('On new page sending request')
//         $.ajax({
//             url: 'https://stark-retreat-48003.herokuapp.com/view_profile',
//             type: 'POST',
//             data: JSON.stringify(obt),
//             contentType: 'application/json',
//             dataType: 'json',
//             success: (msg) => {
//                 window.location = "profile.html"
//                 alert('inside success')
//                 console.log(msg)
//                 // alert(token)
//             },
//             error: (err) => {
//                 console.log(err)
//             }
//         })
//         $.ajax({
//             url: 'https://stark-retreat-48003.herokuapp.com/view_profile',
//             method: 'GET',
//             contentType: 'application/JSON',
//             success: function (msg) {
//                 console.log(msg)
//             },
//             error: function (err) {
//                 console.log(err)
//             }
//         })

//         $(".details").on("click", ".fa-check", function (e) {
//             ob1.token = token
//             ob1.fullname = document.getElementById("fullname").value;
//             ob1.email = document.getElementById("email").value;
//             ob1.password = document.getElementById("confirmpass").value;
//             ob1.new_password = document.getElementById("newpass").value;
//             ob1.confirm_new_password = document.getElementById("confirmnewpass").value;

//             console.log(JSON.stringify(ob1))
//             $.ajax({
//                 url: 'https://stark-retreat-48003.herokuapp.com/edit_profile',
//                 type: 'POST',
//                 data: JSON.stringify(ob1),
//                 contentType: 'application/json',
//                 success: function (msg) {
//                     console.log(msg)
//                 },
//                 error: function (err) {
//                     console.log(err)
//                 }

//             })

//             //forgot password
//             $.ajax({
//                 url: 'https://stark-retreat-48003.herokuapp.com/edit_profile',
//                 type: 'POST',
//                 data: JSON.stringify({
//                     "username": document.getElementById("fullname").value,
//                     "password": document.getElementById("confirmpass").value,
//                     "new_password": document.getElementById("newpass").value,
//                     "confirm_new_password": document.getElementById("confirmnewpass")
//                         .value

//                 }),
//                 contentType: 'application/json',
//                 success: function (msg) {
//                     console.log(msg)
//                 },
//                 error: function (err) {
//                     console.log(err)
//                 }

//             })
//         })
//     }
// });