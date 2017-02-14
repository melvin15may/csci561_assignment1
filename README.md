# CSCI561 Assignment 1

The	 Los	Angeles	 Lakers	are	 playing	against	 their	 rivals	 the	Boston	Celtics	 tonight.		 Lakers	 star	
Jordan	Clarkson wants	to	arrive	earlier	today	to	prepare	himself	for	the	game,	and	he	is	leaving	
from	 his	 mansion	 at	 Newport	 Coast	 to	 Staples	 Center.	 	 As	 everyone	 knows,	 Los	 Angeles	 is	
notorious	for	its	traffic.		Driving	his	2016 Lamborghini Aventador,	Jordan definitely	does	not	want	
to	 be	 stuck	in	 traffic.		 Please	 help	Jordan find	a	 route	 to	get	 him	 to	Staples	 Center	as	 fast	as	
possible.			

To	accomplish	this,	you	will	be	given	a	list	of	freeway	or	road	intersections	(i.e.,	locations) and	
the	time	it	would	take	to	travel	from	there	to	other	freeway	or	road	intersections.		You	will	be	
required	 to	create	a	program	that	finds	 the	 fastest	 route	Jordan must	 travel	 to	get	 to	Staples	
Center.		Your	program	should run	on	vocareum.com using	one	of	the	languages	and	compiler	
supported	by	that	platform.	Your	program	will	be	graded	on	vocareum.	

Your	program	will	be	given live	traffic information in	the	input.txt	file,	which	is	an	arbitrarily	large	
list	of	current	traveling	times	between	intersections/locations.		An	example	live	traffic	data would	
be	a	list	of	intersections	to	intersections	with	traveling	time	(in	minutes), in	the	following	format
(see	below	for	the	full	specification	of	input.txt):

JordanHome CA73/NewportCoastDr 5
CA73/NewportCoastDr I405/CA73 10
I405/CA73 I110/I405 25
I110/I405 I10/I110 20
I10/I110 I110/I405 30
I10/I110 I10/I405 9
I105/I110 I10/I110 7
I10/I110 StaplesCenter 3

Traveling	time	may	not	be the	same	for	both	directions.	For	example,	in	the	above:
I110/I405 I10/I110 20
indicates	that	it	takes	20	minutes	to	travel	from	I110/I405 to	I10/I110 (northbound	as	
you	follow	the	110	freeway),	but
I10/I110 I110/I405 30
indicates	that	it	takes	30	minutes	in	the	other	direction	(southbound).

Beside	live	traffic	information,	Jordan also	has	an	idea	of	how	long	it	takes	on	a	traffic-free	Sunday	
from	 each	 intersection/location	 to	 StaplesCenter.	 	 Hence,	 the	 input.txt	 file	 will	 also	 contain
Jordan's Sunday	traffic estimate	 of	 traveling	 time from	 each	 location	 listed	 in	 the	 file	 to	 his	
destination,	 which	 is	 also	 an	 arbitrarily	 large	 list	 of	 intersections/locations with	 estimated	
traveling	time	(in	minutes) from	there to	StaplesCenter	on	a	traffic-free	Sunday:

JordanHome 55
CA73/NewportCoastDr 50
I405/CA73 40
I110/I405 28
I10/I110 8
I10/I405 39
I105/I110 23
StaplesCenter 0

Your	program	should	write	in	output.txt	the	list of	intersections/locations	traveled	over	in	your	
solution	path,	including	the	starting	and	finishing	locations and	the	accumulated time	from	start
to	that	intersection/location,	in	order	of	travel,	for	example:

JordanHome 0
CA73/NewportCoastDr 5
I405/CA73 15
I110/I405 40
I10/I110 60
StaplesCenter 63

You	 must	 solve	 this	 problem	 using	 Breadth-First	 search,	 Depth-First	 Search, Uniform-cost	
Search,	and	A*	Search	separately.	
