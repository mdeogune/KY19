function doPost(e) {
  
  var ss= SpreadsheetApp.openById('1lTqaGco9GRcFq7THZ5IWGrLl3qVWm0T5m0VXzQtPAts');
  var ky_id = e.parameter.ky_id;
  var ca_id = e.parameter.caId;
  var name = e.parameter.full_name;
  var email = e.parameter.email;
  var college = e.parameter.college;
  var year = e.parameter.year;
  var mobile_number = e.parameter.mobile_number;
  var whatsapp_number = e.parameter.whatsapp_number
  var gender = e.parameter.gender;
  var profile_link = e.parameter.profile_link;
  var postal_address = e.parameter.postal_address;
  var pincode = e.parameter.pincode;
  var reason = e.parameter.reason;
  var sheet= ss.getSheetByName('CA Regs 2018');
  
  sheet.appendRow([ky_id, ca_id, name, email, college,year, gender, mobile_number,whatsapp_number,postal_address, pincode, reason, profile_link]);  
  return ContentService.createTextOutput(e);
}