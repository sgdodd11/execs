clear all 

local files revelio_pos_fortune500US_Jan21-Jan22_567.csv revelio_pos_fortune500US_Jan22-Jan23_567.csv revelio_pos_fortune500US_Jan23-Jan24_567.csv revelio_pos_fortune500US_Jan24-Jan25_567.csv revelio_pos_fortune500US_Jan25-Mar25_567.csv


* gen empty tempfile to record IDs to use 
insobs 1 
gen user_id = . 
tempfile allids
save `allids', replace 

* extract and append all userids 
foreach file of local files {
	di "`file'"
	import delimited "data/raw/`file'", clear 

	* just get unique IDs 
	duplicates drop user_id, force 
		
	keep user_id 
	
	append using `allids'
	save `allids', replace 
}

use `allids', clear 
drop if user_id==. 
duplicates drop user_id, force  

export delimited using "data/ids_revelio_pos_fortune500US_Jan21-Mar25_567.csv", replace  
