#!usr/bin/env python
#
#<sixie6e@paracosmoclast>
#
'''
remove special waters, remove variable sizes, govt/corporate control balance, total nat potable, gallons sold, municipal water levels, ocean/lake/river/stream levels
'''
import pandas as pd
import matplotlib

wastewater_untreated= 80% #returns to the ground this way
using_safeService = 70%, 5300000000 #located on premises, available when needed, and free from contamination.
using_basicService = 90%, 6800000000 #basic service is an improved drinking-water source within a round trip of 30 minutes to collect water.
sans_basicService = 785000000
surface_dependent = 144000000

#using 2019 annual base
def america():
	sizes = {
	'1oz':12.3, '6oz':12.3, '8oz':12.3, '10oz':12.3, '10.1oz':12.3, '11.15oz':12.3, '12oz':12.3, '14oz':12.3, '16oz':12.3, '16.9oz':12.3, '17oz':12.3, '18oz':12.3, '20oz':12.3, '23oz':12.3,'23.7oz':12.3, '25.3oz':12.3, '30.4oz':12.3, '33.8oz':12.3, '50.7oz':12.3, '101.4oz':12.3, '202.8oz':12.3, '676oz':12.3,'500mL':12.3, '600mL':12.3, '700mL':12.3, '1L':12.3, '1.5L':12.3, '1G':12.3, '5G':12.3}
	
	prices = {
	'1oz':12.3, '6oz':12.3, '8oz':12.3, '10oz':12.3, '10.1oz':12.3, '11.15oz':12.3, '12oz':12.3, '14oz':12.3, '16oz':12.3, '16.9oz':12.3, '17oz':12.3, '18oz':12.3, '20oz':12.3, '23oz':12.3,'23.7oz':12.3, '25.3oz':12.3, '30.4oz':12.3, '33.8oz':12.3, '50.7oz':12.3, '101.4oz':12.3, '202.8oz':12.3, '676oz':12.3,'500mL':12.3, '600mL':12.3, '700mL':12.3, '1L':12.3, '1.5L':12.3, '1G':12.3, '5G':12.3}
	
	per_capita = {	
	'2009':27.2, '2010':27.8, '2011':28.7, '2012': 30.4, '2013':31.6, '2014':33.6, '2015':35.9, '2016':38.5, '2017':40.6, '2018':42.4, '2019':43.7}
	
	per_state = {	
	'al':27.2, 'az':28.7, 'ar': 30.4, 'ca':31.6, 'co':33.6, 'ct':35.9, 'de':38.5, 'fl':40.6, 'ga':42.4, 'id':27.2, 'il':27.8, 'in':28.7, 'ia':30.4, 'ks':31.6, 'ky':33.6, 'la':35.9, 'me':38.5, 'md':40.6, 'ma':42.4, 'mi':43.7, 'mn':27.2, 'ms':27.8, 'mo':28.7, 'mt':30.4, 'ne':31.6, 'nv':33.6, 'nh':35.9, 'nj':38.5, 'nm':40.6, 'ny':42.4, 'nc':43.7, 'nd':27.2, 'oh':27.8, 'ok':28.7, 'or':30.4, 'pa':31.6, 'ri':33.6, 'sc':35.9, 'sd':38.5, 'tn':40.6, 'tx':42.4, 'ut':43.7, 'vt':27.2, 'va':27.8, 'wa':28.7, 'wv':30.4, 'wi':31.6, 'wy':33.6}
	
	#'ak':27.8, 'hi':43.7

	

	brands = ["3 springs", "3300 artesian water", "365 spring water", "a. l. lee corporation natural spring water", "aafiya water", "aarp west virginia", "abita springs", "absopure distilled water", "absopure drinking water", "absopure natural spring water", "admiral dewey distilled water", "admiral dewey drinking water", "admiral dewey purified water", "adobe springs", "aguazul natural spring water", "alaska chill", "alaska glacier", "alaska glacier cap", "alaska glacierblend", "alaska natural spring water", "albion water", "alcatraz", "alhambra", "alps water", "amelia springs water", "angel fire", "apani", "appalachian springs water", "aquamantra", "aquafina", "aquoforce", "arbutus", "arctic mist", "arrowhead", "artesia", "av-02", "avita", "baccara", "bashas' artesian spring water", "belmont springs", "big bear mountain", "big indian", "bikers' coolant","black mountain spring water", "bonaqa", "brick house farm water", "calistoga mineral water", "calistoga mountain spring water", "calistoga spring water","carolina mountain spring water", "caroline mountain water", "carrabassett", "castle rock", "castle springs", "catskill mountains", "cerebellum h2o", "cherokee bottled water", "claire baie bottled water", "clear mountain", "clearly arctic", "climax ky", "cobb mountain natural spring water", "cole brothers", "colfax", "colorado crystal", "cool luc", "cool springs pure springwater", "country creek", "crystal geyser natural alpine spring water", "crystal geyser natural spring water", "crystal geyser water", "crystal springs", "dannon", "dasani","deep rock", "deep rock crystal drop", "deep rock fontenelle", "deer park maryland", "deer park pennsylvania", "diamond natural spring water", "distillata", "dog water", "drinka", "earth2o", "edins x.o.", "eldorado natural spring water", "english mountain", "evo premium water", "famous crazy natural mineral water", "famous natural deep well mineral water", "famous premium drinking water", "flo first liquid obsession", "food lion drinking water", "fountain natural spring water", "fountainhead", "franklin heritage", "georgia mountain water", "giant filtered drinking water", "giant springs", "glaceau smart water", "glaceau vitamin water", "glenwood inglewood", "grand springs", "great bear", "h2only", "halstead", "harris teeter natural spring water", "hawaii water", "hd2o", "hidden spring", "hillcrest spring water. inc.", "hinckley springs", "hinkley & schmidt", "ice mountain", "idaho ice", "indian hills spring water", "keeper springs", "kentwood springs", "kroger drinking water", "kroger spring water", "laure spring water", "lauré pristine spring water", "le-natures water", "leisure time", "lesage natural wells", "life o2", "loon county", "manitou mineral water", "marin county all natural", "mckenzie mist", "model on a bottle (tm)", "mount olympus", "mountain forest spring water", "mountaineer pure", "mt. mckinley clear", "naturalle mountain spring water", "noah's california spring water", "oasis", "odwalla", "original fountain of youth mineral water", "ozardar", "ozarka", "pagosa springs", "palomar mountain spring water", "panther creek", "paradise bottled water", "parley's canyon", "penta", "pine barrens", "pocono springs pure mountain spring water", "poland spring", "pristine peaks", "pure montana", "pure pride", "purely sedona", "purple parrot", "quibell", "rain", "rocky grove", "saegertown beverage eureka springs", "seven creeks spring water", "shenandoah spring water", "shivar springs", "sierra springs", "silver creek",  "snow valley mountain spring water", "snowbird", "snowline natural water", "sparkletts", "stoneclear springs", "sweet springs natural mountain water", "tennessee mountain pure spring water", "trinity springs", "triton purified drinking water", "utopia", "valentine's pure spring water", "valley of the moon", "vermont pure", "water boy", "west virginia's pride of the mountains", "whispering springs water", "whole foods market 365 distilled water", "whole foods market 365 italian sparkling mineral water", "whole foods market 365 spring water", "wissahickon mountain spring water", "yellowstone headwaters", "zephyrhills"]

	ann_rainfall = {	
	'al':56.27, , 'az':14.71, 'ar': 65.59, 'ca':29.1, 'co':18.86, 'ct':54.24, 'de':41.58, 'fl':52.02, 'ga':47.89, 'id':23.34, 'il':49.87, 'in':49.52, 'ia':41.63, 'ks':36.08, 'ky':61.28, 'la':61.9, 'me':49.94, 'md':42.63, 'ma':52.7, 'mi':41.79, 'mn':35.49, 'ms':68.06, 'mo':53.85, 'mt':21.41, 'ne':31.41, 'nv':13.77, 'nh':50.2, 'nj':51.89, 'nm':13.35, 'ny':48.18, 'nc':50.98, 'nd':24.34, 'oh':46.86, 'ok':44.94, 'or':30.01, 'pa':50.75, 'ri':57.13, 'sc':45.71, 'sd':31.42, 'tn':66.87, 'tx':26.87, 'ut':16.94, 'vt':51.41, 'va':46.0, 'wa':33.08, 'wv':48.24, 'wi':44.55, 'wy':18.29}
	
	#'ak':37.33, 'hi':70.0
	
#####################################

worldwide_sales = [
"wholesale":19400000000, "retail":34600000000]

#####################################
india = []
france = []
germany = []
italy = []
thailand = []
brazil = []
indonesia = []
mexico = []
china = []




