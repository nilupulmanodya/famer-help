var province_arr = new Array("Central","Western","Eastern","North Central","Northern","North Western","Sabaragamuwa","Southern","Uva");

var district = new Array();
district[0]=" ";
district[1]="Kandy | Matale | Nuwara Eliya";
district[2]="Colombo | Gampaha | Kalutara";
district[3]="Ampara | Batticaloa | Trincomalee";
district[4]="Anuradhapura |Polonnaruwa";
district[5]="Jaffna | Kilinochchi | Mannar | Mullaitivu | Vavuniya";
district[6]="Kurunegala | Puttalam";
district[7]="Kegalle | Ratnapura";
district[8]="Galle | Hambantota | Matara";
district[9]="Badulla | Monaragala";


function print_province(province_id){
	// given the id of the <select> tag as function argument, it inserts <option> tags
	var option_str = document.getElementById(province_id);
	option_str.length=0;
	option_str.options[0] = new Option('Select Province','');
	option_str.selectedIndex = 0;
	for (var i=0; i<province_arr.length; i++) {
		option_str.options[option_str.length] = new Option(province_arr[i],province_arr[i]);
	}
}

function print_district(district_id, district_index){
	var option_str = document.getElementById(district_id);
	option_str.length=0;	
	option_str.options[0] = new Option('Select District','');
	option_str.selectedIndex = 0;
	var district_arr = district[district_index].split("|");
	for (var i=0; i<district_arr.length; i++) {
		option_str.options[option_str.length] = new Option(district_arr[i],district_arr[i]);
	}
}
