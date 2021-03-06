from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import datetime
app = Flask(__name__)

data = [
{
"Id": 1,
"Title": "Moonrise Through Mauna Kea's Shadow",
"Poster": "https://apod.nasa.gov/apod/image/1903/moonrisemk_connelley_1600.jpg",
"Year": 2019,
"Month": 3,
"Day": 10,
"Explanation": "How can the Moon rise through a mountain? It cannot -- what was photographed here is a moonrise through the shadow of a large volcano. The volcano is Mauna Kea, Hawai'i, USA, a frequent spot for spectacular photographs since it is one of the premier observing locations on planet Earth. The Sun has just set in the opposite direction, behind the camera. Additionally, the Moon has just passed full phase -- were it precisely at full phase it would rise, possibly eclipsed, at the very peak of the shadow. The Moon is actually rising in the triangular shadow cone of the volcano, a corridor of darkness that tapers off in the distance like converging train tracks. The Moon is too large and too far away to be affected by the shadow of the volcano. Refraction of moonlight through the Earth's atmosphere makes the Moon appear slightly oval. Cinder cones from old volcanic eruptions are visible in the foreground.",
"Copyright": "Michael Connelley(U. Hawaii)",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 2,
"Title": "Crescent Enceladus",
"Poster": "https://apod.nasa.gov/apod/image/1903/PIA20522enceladus.jpg",
"Year": 2019,
"Month": 3,
"Day": 9,
"Explanation": "Peering from the shadows, the Saturn-facing hemisphere of tantalizing inner moon Enceladus poses in this Cassini spacecraft image. North is up in the dramatic scene captured during November 2016 as Cassini's camera was pointed in a nearly sunward direction about 130,000 kilometers from the moon's bright crescent. In fact, the distant world reflects over 90 percent of the sunlight it receives, giving its surface about the same reflectivity as fresh snow. A mere 500 kilometers in diameter, Enceladus is a surprisingly active moon. Data collected during Cassini's flybys and years of images have revealed the presence of remarkable south polar geysers and a possible global ocean of liquid water beneath an icy crust.",
"Copyright": "Cassini Imaging Team, SSI, JPL, ESA, NASA",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 3,
"Title": "Stardust and Starlight in M78",
"Poster": "https://apod.nasa.gov/apod/image/1903/M78_RGBwright.jpg",
"Year": 2019,
"Month": 3,
"Day": 8,
"Explanation": "Interstellar dust clouds and bright nebulae abound in the fertile constellation of Orion. One of the brightest, M78, is near the center in this colorful telescopic view, covering an area north of Orion's belt. At a distance of about 1,500 light-years, the bluish nebula itself is about 5 light-years across. Its blue tint is due to dust preferentially reflecting the blue light of hot, young stars in the region. Dark dust lanes and other nebulae can easily be traced through the gorgeous skyscape that includes many Herbig- Haro objects, energetic jets from stars in the process of formation. But missing from this image is McNeil's nebula. A major discovery only recognized in 2004, the enigmatic, variable nebula was found along the dark lane of dust above and right of larger M78. McNeil's nebula is associated with a protostar and seen to be sometimes present and sometimes absent in photos of the well-imaged region. McNeil's nebula faded from view late last year and is still absent in this deep image recorded in February 2019.",
"Copyright": "Richard S. Wright Jr.",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 4,
"Title": "Sharpless 249 and the Jellyfish Nebula",
"Poster": "https://apod.nasa.gov/apod/image/1903/F_JellyFish_FIN_APOD.jpg",
"Year": 2019,
"Month": 3,
"Day": 7,
"Explanation": "Normally faint and elusive, the Jellyfish Nebula is caught in this alluring telescopic field of view. The entire scene is a two panel mosaic constructed using narrowband image data, with emission from sulfur, hydrogen and oxygen atoms shown in red, green and blue hues. It's anchored right and left by two bright stars, Mu and Eta Geminorum, at the foot of the celestial twin. The Jellyfish Nebula itself is right of center, the brighter arcing ridge of emission with dangling tentacles. In fact, the cosmic jellyfish is part of bubble-shaped supernova remnant IC 443, the expanding debris cloud from a massive star that exploded. Light from the explosion first reached planet Earth over 30,000 years ago. Like its cousin in astrophysical waters the Crab Nebula supernova remnant, the Jellyfish Nebula is known to harbor a neutron star, the remnant of the collapsed stellar core. An emission nebula cataloged as Sharpless 249 fills the field at the upper left. The Jellyfish Nebula is about 5,000 light-years away. At that distance, this image would be about 300 light-years across.",
"Copyright": "Data - Steve Milne & Barry Wilson,Processing -Steve Milne",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 5,
"Title": "A February without Sunspots",
"Poster": "https://apod.nasa.gov/apod/image/1903/SunMaxMin_Friedman_1733.jpg",
"Year": 2019,
"Month": 3,
"Day": 6,
"Explanation": "Where have all the sunspots gone? Last month the total number of spots that crossed our Sun was ... zero. Well below of the long term monthly average, the Sun's surface has become as unusually passive this solar minimum just like it did 11 years ago during the last solar minimum. Such passivity is not just a visual spectacle, it correlates with the Sun being slightly dimmer, with holes in the Sun's corona being more stable, and with a reduced intensity in the outflowing solar wind. The reduced wind, in turn, cools and collapses Earth's outer atmosphere (the thermosphere), causing reduced drag on many Earth-orbiting satellites. Pictured in inverted black & white on the left, the Sun's busy surface is shown near solar maximum in 2012, in contrast to the image on the right, which shows the Sun's surface last August, already without spots (for a few days), as solar minimum was setting in. Effects of this unusually static solar minimum are being studied.",
"Copyright": "Alan Friedman(Averted Imagination)",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 6,
"Title": "X-Ray Superbubbles in Galaxy NGC 3079",
"Poster": "https://apod.nasa.gov/apod/image/1903/ngc3079Superbubbles_chandra_1080.jpg",
"Year": 2019,
"Month": 3,
"Day": 5,
"Explanation": "What created these huge galactic superbubbles? Two of these unusual bubbles, each spanning thousands of light-years, were recently discovered near the center of spiral galaxy NGC 3079. The superbubbles, shown in purple on the image right, are so hot they emit X-rays detected by NASA's Earth-orbiting Chandra X-Ray Observatory. Since the bubbles straddle the center of NGC 3079, a leading hypothesis is that they were somehow created by the interaction of the central supermassive black hole with surrounding gas. Alternatively, the superbubbles might have been created primarily by the energetic winds from many young and hot stars near that galaxy's center. The only similar known phenomenon is the gamma-ray emitting Fermi bubbles emanating from the center of our Milky Way Galaxy, discovered 10 years ago in images taken by NASA's Fermi satellite. Research into the nature of the NGC 3079 superbubbles will surely continue, as well as searches for high-energy superbubbles in other galaxies.",
"Copyright": "NASA, STScI",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 7,
"Title": "Celestial Alignment over Sicilian Shore",
"Poster": "https://apod.nasa.gov/apod/image/1903/MoonPlanetsStar_Giannobile_1313.jpg",
"Year": 2019,
"Month": 3,
"Day": 4,
"Explanation": "This was a sunrise to remember. About a month ago, just before the dawn of the Sun, an impressive alignment of celestial objects was on display to the east. Pictured, brightest and closest to the horizon, is the Moon. The Moon's orange glow is caused by the scattering away of blue light by the intervening atmosphere. Next brightest and next closest to the horizon is the planet Venus. Compared to the Moon, Venus appears more blue -- as can (also) be seen in its reflection from the water. Next up is Jupiter, while the bright object above Jupiter is the star Antares. Although this display was visible from almost anywhere on planet Earth, the featured image was taken along a picturesque seashore near the city of Syracuse, on the island of Sicily, in the country of Italy. This month Saturn appears between Venus and Jupiter before sunrise, while Mars is visible just after sunset.",
"Copyright": "Dario Giannobile",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 8,
"Title": "The Orion Bullets",
"Poster": "https://apod.nasa.gov/apod/image/1903/OrionBullets_Gemini_2592.jpg",
"Year": 2019,
"Month": 3,
"Day": 3,
"Explanation": "Why are bullets of gas shooting out of the Orion Nebula? Nobody is yet sure. First discovered in 1983, each bullet is actually about the size of our Solar System, and moving at about 400 km/sec from a central source dubbed IRc2. The age of the bullets, which can be found from their speed and distance from IRc2, is very young -- typically less than 1,000 years. As the bullets expand out the top of the Kleinmann-Low section of the Orion Nebula, a small percentage of iron gas causes the tip of each bullet to glow blue, while each bullet leaves a tubular pillar that glows by the light of heated hydrogen gas.  The detailed image was created using the 8.1 meter Gemini South telescope in Chile with an adaptive optics system (GeMS). GeMS uses five laser generated guide stars to help compensate for the blurring effects of planet Earth's atmosphere.",
"Copyright": "Rodrigo Carrasco (Gemini Obs.),Travis Rector(Univ. Alaska Anchorage)",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 9,
"Title": "NGC 6302: The Butterfly Nebula",
"Poster": "https://apod.nasa.gov/apod/image/1903/NGC6302_ButterflyNebula_NASA.jpg",
"Year": 2019,
"Month": 3,
"Day": 2,
"Explanation": "The bright clusters and nebulae of planet Earth's night sky are often named for flowers or insects. Though its wingspan covers over 3 light-years, NGC 6302 is no exception. With an estimated surface temperature of about 250,000 degrees C, the dying central star of this particular planetary nebula has become exceptionally hot, shining brightly in ultraviolet light but hidden from direct view by a dense torus of dust. This sharp close-up was recorded by the Hubble Space Telescope in 2009. The Hubble image data is reprocessed here, showing off the remarkable details of the complex planetary nebula. Cutting across a bright cavity of ionized gas, the dust torus surrounding the central star is near the center of this view, almost edge-on to the line-of-sight. Molecular hydrogen has been detected in the hot star's dusty cosmic shroud. NGC 6302 lies about 4,000 light-years away in the arachnologically correct constellation of the Scorpion (Scorpius).",
"Copyright": "Robert Eder",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 10,
"Title": "A Charioteer's Comet",
"Poster": "https://apod.nasa.gov/apod/image/1903/rolando-ligustri-C2018Y1_190227_FB_1551288721.jpg",
"Year": 2019,
"Month": 3,
"Day": 1,
"Explanation": "Still racing across planet Earth's night skies, Comet Iwamoto (C/2018 Y1) shares this pretty telescopic field of view with stars and nebulae of northern constellation Auriga, the Charioteer. Captured on February 27, Iwamoto's greenish coma and faint tail appear between a complex of reddish emission nebulae and open star cluster M36 (bottom right). The reddish emission is light from hydrogen gas ionized by ultraviolet radiation from hot stars near the region's giant molecular cloud some 6,000 light-years distant. The greenish glow from the comet, less than 5 light-minutes away, is predominantly emission from diatomic carbon molecules fluorescing in sunlight. M36, one of Auriga's more familiar star clusters, is also a background object far beyond the Solar System, about 4,000 light-years away. Comet Iwamoto passed closest to Earth on February 12 and is outward bound in a highly elliptical orbit that will carry it beyond the Kuiper belt. With an estimated orbital period of 1,317 years it should return to the inner Solar System in 3390 AD.",
"Copyright": "Rolando Ligustri(CARA Project,CAST)",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 11,
"Title": "Sharpest Ultima Thule",
"Poster": "https://apod.nasa.gov/apod/image/1902/ultima-thule-1-ca06_022219.png",
"Year": 2019,
"Month": 2,
"Day": 28,
"Explanation": "On January 1, New Horizons swooped to within 3,500 kilometers of the Kuiper Belt world known as Ultima Thule. That's about 3 times closer than its July 2015 closest approach to Pluto. The spacecraft's unprecedented feat of navigational precision, supported by data from ground and space-based observing campaigns, was accomplished 6.6 billion kilometers (over 6 light-hours) from planet Earth. Six and a half minutes before closest approach to Ultima Thule it captured the nine frames used in this composite image. The most detailed picture possible of the farthest object ever explored, the image has a resolution of about 33 meters per pixel, revealing intriguing bright surface features and dark shadows near the terminator. A primitive Solar System object, Ultima Thule's two lobes combine to span just 30 kilometers. The larger lobe, referred to as Ultima, is recently understood to be flattened like a fluffy pancake, while the smaller, Thule, has a shape that resembles a dented walnut.",
"Copyright": "NASA,Johns Hopkins University APL,Southwest Research Institute,National Optical Astronomy Observatory",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 12,
"Title": "Magnetic Orion",
"Poster": "https://apod.nasa.gov/apod/image/1902/MagneticOrion_EsoSofia_1833.jpg",
"Year": 2019,
"Month": 2,
"Day": 27,
"Explanation": "Can magnetism affect how stars form? Recent analysis of Orion data from the HAWC+ instrument on the airborne SOFIA observatory indicate that, at times, it can. HAWC+ is able to measure the polarization of far-infrared light which can reveal the alignment of dust grains by expansive ambient magnetic fields. In the featured image, these magnetic fields are shown as curvy lines superposed on an infrared image of the Orion Nebula taken by a Very Large Telescope in Chile. Orion's Kleinmann-Low Nebula is visible slightly to the upper right of the image center, while bright stars of the Trapezium cluster are visible just to the lower left of center. The Orion Nebula at about l300 light years distant is the nearest major star formation region to the Sun.",
"Copyright": "NASA, SOFIA, D. Chuss et al. & ESO, M. McCaughrean et al.",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 13,
"Title": "Simulation TNG50: A Galaxy Cluster Forms",
"Poster": "https://www.youtube.com/embed/cNT5yAqpBmI?rel=0",
"Year": 2019,
"Month": 2,
"Day": 26,
"Explanation": "How do clusters of galaxies form? Since our universe moves too slowly to watch, faster-moving computer simulations are created to help find out. A recent effort is TNG50 from IllustrisTNG, an upgrade of the famous Illustris Simulation. The first part of the featured video tracks cosmic gas (mostly hydrogen) as it evolves into galaxies and galaxy clusters from the early universe to today, with brighter colors marking faster moving gas. As the universe matures, gas falls into gravitational wells, galaxies forms, galaxies spin, galaxies collide and merge, all while black holes form in galaxy centers and expel surrounding gas at high speeds. The second half of the video switches to tracking stars, showing a galaxy cluster coming together complete with tidal tails and stellar streams. The outflow from black holes in TNG50 is surprisingly complex and details are being compared with our real universe. Studying how gas coalesced in the early universe helps humanity better understand how our Earth, Sun, and Solar System originally formed.",
"Copyright": "IllustrisTNG Project, Dylan Nelson, Symphony No. 5 (Ludwig van Beethoven)",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 14,
"Title": "Red Sprite Lightning over Kununurra",
"Poster": "https://apod.nasa.gov/apod/image/1902/RedSprites_Broady_3000.jpg",
"Year": 2019,
"Month": 2,
"Day": 25,
"Explanation": "What are those red filaments in the sky? It is a rarely seen form of lightning confirmed only about 30 years ago: red sprites. Recent research has shown that following a powerful positive cloud-to-ground lightning strike, red sprites may start as 100-meter balls of ionized air that shoot down from about 80-km high at 10 percent the speed of light and are quickly followed by a group of upward streaking ionized balls. The featured image, taken just over a week ago in Kununurra, Western Australia, captured some red sprites while shooting a time-lapse sequence of a distant lightning storm. Pictured, green trees cover the foreground, dark mountains are seen on the horizon, ominous storm clouds hover over the distant land, while red sprites appear in front of stars far in the distance. Red sprites take only a fraction of a second to occur and are best seen when powerful thunderstorms are visible from the side.",
"Copyright": "Ben Broady",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 15,
"Title": "The Expanding Echoes of Supernova 1987A",
"Poster": "https://apod.nasa.gov/apod/https://en.wikipedia.org/wiki/Bullseye_(target)",
"Year": 2019,
"Month": 2,
"Day": 24,
"Explanation": "Can you find supernova 1987A? It isn't hard -- it occurred at the center of the expanding bullseye pattern. Although this stellar detonation was first seen in 1987, light from SN 1987A continued to bounce off clumps of interstellar dust and be reflected to us even many years later. Light echoes recorded between 1988 and 1992 by the Anglo Australian Telescope (AAT) in Australia are shown moving out from the position of the supernova in the featured time-lapse sequence. These images were composed by subtracting an LMC image taken before the supernova light arrived from later LMC images that included the supernova echo. Other prominent light echo sequences include those taken by the EROS2 and SuperMACHO sky monitoring projects. Studies of expanding light echo rings around other supernovas have enabled more accurate determinations of the location, date, and symmetry of these tremendous stellar explosions. Yesterday marked the 32nd anniversary of SN 1987A: the last recorded supernova in or around our Milky Way Galaxy, and the last to be visible to the unaided eye.",
"Copyright": "David Malin, AAT",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 16,
"Title": "The Stars of the Triangulum Galaxy",
"Poster": "https://apod.nasa.gov/apod/image/1902/heic1901aTriangulum.jpg",
"Year": 2019,
"Month": 2,
"Day": 23,
"Explanation": "Like grains of sand on a cosmic beach, stars of the Triangulum Galaxy are resolved in this sharp mosaic from the Hubble Space Telescope's Advanced Camera for Surveys (ACS). The inner region of the galaxy spanning over 17,000 light-years is covered at extreme resolution, the second largest image ever released by Hubble. At its center is the bright, densely packed galactic core surrounded by a loose array of dark dust lanes mixed with the stars in the galactic plane. Also known as M33, the face-on spiral galaxy lies 3 million light-years away in the small northern constellation Triangulum. Over 50,000 light-years in diameter, the Triangulum Galaxy is the third largest in the Local Group of galaxies after the Andromeda Galaxy (M31), and our own Milky Way. Of course, to fully appreciate the Triangulum's stars, star clusters, and bright nebulae captured in this Hubble mosaic, you'll need to use a zoom tool.",
"Copyright": "NASA,ESA,M. Durbin, J. Dalcanton, and B. F. Williams(University of Washington)",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 17,
"Title": "NGC 4565: Galaxy on Edge",
"Poster": "https://apod.nasa.gov/apod/image/1902/N4565ps06d_35tp_Kaltseis2019.jpg",
"Year": 2019,
"Month": 2,
"Day": 22,
"Explanation": "Magnificent spiral galaxy NGC 4565 is viewed edge-on from planet Earth. Also known as the Needle Galaxy for its narrow profile, bright NGC 4565 is a stop on many telescopic tours of the northern sky, in the faint but well-groomed constellation Coma Berenices. This sharp, colorful image reveals the galaxy's boxy, bulging central core cut by obscuring dust lanes that lace NGC 4565's thin galactic plane. An assortment of other background galaxies is included in the pretty field of view, with neighboring galaxy NGC 4562 at the upper right. NGC 4565 itself lies about 40 million light-years distant and spans some 100,000 light-years. Easily spotted with small telescopes, sky enthusiasts consider NGC 4565 to be a prominent celestial masterpiece Messier missed.",
"Copyright": "Christoph Kaltseis,CEDIC",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 18,
"Title": "Reflections on vdB 9",
"Poster": "https://apod.nasa.gov/apod/image/1902/20181013VDB9kerschhuber.jpg",
"Year": 2019,
"Month": 2,
"Day": 21,
"Explanation": "Centered in a well-composed celestial still life, pretty, blue vdB 9 is the 9th object in Sidney van den Bergh's 1966 catalog of reflection nebulae. It shares this telescopic field of view, about twice the size of a full moon on the sky, with stars and dark, obscuring dust clouds in the northerly constellation Cassiopeia. Cosmic dust is preferentially reflecting blue starlight from embedded, hot star SU Cassiopeiae, giving vdB 9 the characteristic bluish tint associated with a classical reflection nebula. SU Cas is a Cepheid variable star, though even at its brightest it is just too faint to be seen with the unaided eye. Still Cepheids play an important role in determining distances in our galaxy and beyond. At the star's well-known distance of 1,540 light-years, this cosmic canvas would be about 24 light-years across.",
"Copyright": "Guenter Kerschhuber",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 19,
"Title": "Doomed Star Eta Carinae",
"Poster": "https://apod.nasa.gov/apod/image/1902/EtaCarinae_HubbleSchmidt_1764.jpg",
"Year": 2019,
"Month": 2,
"Day": 20,
"Explanation": "Eta Carinae may be about to explode. But no one knows when - it may be next year, it may be one million years from now. Eta Carinae's mass - about 100 times greater than our Sun - makes it an excellent candidate for a full blown supernova. Historical records do show that about 170 years ago Eta Carinae underwent an unusual outburst that made it one of the brightest stars in the southern sky. Eta Carinae, in the Keyhole Nebula, is the only star currently thought to emit natural LASER light. This featured image brings out details in the unusual nebula that surrounds this rogue star. Diffraction spikes, caused by the telescope, are visible as bright multi-colored streaks emanating from Eta Carinae's center. Two distinct lobes of the Homunculus Nebula encompass the hot central region, while some strange radial streaks are visible in red extending toward the image right. The lobes are filled with lanes of gas and dust which absorb the blue and ultraviolet light emitted near the center. The streaks, however, remain unexplained.",
"Copyright": "Judy Schmidt",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 20,
"Title": "Comet Iwamoto Before Spiral Galaxy NGC 2903",
"Poster": "https://apod.nasa.gov/apod/https://en.wikipedia.org/wiki/C/2018_Y1_(Iwamoto)",
"Year": 2019,
"Month": 2,
"Day": 19,
"Explanation": "It isn't every night that a comet passes a galaxy. Last Thursday, though, binocular comet C/2018 Y1 (Iwamoto) moved nearly in front of a spiral galaxy of approximately the same brightness: NGC 2903. Comet Iwamoto was discovered late last year and orbits the Sun in a long ellipse. It last visited the inner Solar System during the Middle Ages, around the year 648. The comet reached its closest point to the Sun -- between Earth and Mars -- on February 6, and its closest point to Earth a few days ago, on February 13. The featured time-lapse video condenses almost three hours into about ten seconds, and was captured last week from Switzerland. At that time Comet Iwamoto, sporting a green coma, was about 10 light minutes distant, while spiral galaxy NGC 2903 remained about 30 million light years away. Two satellites zip diagonally through the field about a third of the way through the video. Typically, a few comets each year become as bright as Comet Iwamoto.",
"Copyright": "Norbert Span",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 21,
"Title": "Dragon Aurora over Iceland",
"Poster": "https://apod.nasa.gov/apod/image/1902/DragonAurora_Zhang_2241.jpg",
"Year": 2019,
"Month": 2,
"Day": 18,
"Explanation": "Have you ever seen a dragon in the sky? Although real flying dragons don't exist, a huge dragon-shaped aurora developed in the sky over Iceland earlier this month. The aurora was caused by a hole in the Sun's corona that expelled charged particles into a solar wind that followed a changing interplanetary magnetic field to Earth's magnetosphere. As some of those particles then struck Earth's atmosphere, they excited atoms which subsequently emitted light: aurora. This iconic display was so enthralling that the photographer's mother ran out to see it and was captured in the foreground. No sunspots have appeared on the Sun so far in February, making the multiple days of picturesque auroral activity this month somewhat surprising.",
"Copyright": "Jingyi Zhang & Wang Zheng",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 22,
"Title": "Shadow of a Martian Robot",
"Poster": "https://apod.nasa.gov/apod/image/1902/marsshadow_opportunity_1024.jpg",
"Year": 2019,
"Month": 2,
"Day": 17,
"Explanation": "What if you saw your shadow on Mars and it wasn't human? Then you might have been the Opportunity rover exploring Mars. Opportunity explored the red planet from 2004 to 2018, finding evidence of ancient water, and sending breathtaking images across the inner Solar System. Pictured here in 2004, Opportunity looks opposite the Sun into Endurance Crater and sees its own shadow. Two wheels are visible on the lower left and right, while the floor and walls of the unusual crater are visible in the background. Caught in a dust storm in 2018, last week NASA stopped trying to contact Opportunity and declared the ground-breaking mission, originally planned for only 92 days, complete.",
"Copyright": "MarsExploration Rover Mission,JPL,NASA",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 23,
"Title": "NGC 2359: Thor's Helmet",
"Poster": "https://apod.nasa.gov/apod/image/1902/thor_LHORHGOBO_final.jpg",
"Year": 2019,
"Month": 2,
"Day": 16,
"Explanation": "NGC 2359 is a helmet-shaped cosmic cloud with wing-like appendages popularly called Thor's Helmet. Heroically sized even for a Norse god, Thor's Helmet is about 30 light-years across. In fact, the helmet is more like an interstellar bubble, blown as a fast wind from the bright, massive star near the bubble's center inflates a region within the surrounding molecular cloud. Known as a Wolf-Rayet star, the central star is an extremely hot giant thought to be in a brief, pre-supernova stage of evolution. NGC 2359 is located about 15,000 light-years away in the constellation Canis Major. The remarkably detailed image is a mixed cocktail of data from broadband and narrowband filters that captures natural looking stars and the glow of the nebula's filamentary structures. It highlights a blue-green color from strong emission due to oxygen atoms in the glowing gas.",
"Copyright": "IgnacioDiaz Bobillo",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 24,
"Title": "Opportunity at Perseverance Valley",
"Poster": "https://apod.nasa.gov/apod/image/1902/OpportunitySol5074_1a_kremer.jpg",
"Year": 2019,
"Month": 2,
"Day": 15,
"Explanation": "Opportunity had already reached Perseverance Valley by June of 2018. Its view is reconstructed in a colorized mosaic of images taken by the Mars Exploration Rover's Navcam. In fact, Perseverance Valley is an appropriate name for the destination. Designed for a 90 day mission, Opportunity had traveled across Mars for over 5,000 sols (martian solar days) following a January 2004 landing in Eagle crater. Covering a total distance of over 45 kilometers (28 miles), its intrepid journey of exploration across the Martian landscape has come to a close here. On June 10, 2018, the last transmission from the solar-powered rover was received as a dust storm engulfed the Red Planet. Though the storm has subsided, eight months of attempts to contact Opportunity have not been successful and its trailblazing mission ended after almost 15 years of exploring the surface of Mars.",
"Copyright": "NASA, JPL-Caltech, Kenneth Kremer, Marco Di Lorenzo",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 25,
"Title": "Solar System Family Portait",
"Poster": "https://apod.nasa.gov/apod/image/1902/ssportrait_vg1_big.jpg",
"Year": 2019,
"Month": 2,
"Day": 14,
"Explanation": "On Valentine's Day in 1990, cruising four billion miles from the Sun, the Voyager 1 spacecraft looked back one last time to make this first ever Solar System family portrait. The complete portrait is a 60 frame mosaic made from a vantage point 32 degrees above the ecliptic plane. In it, Voyager's wide angle camera frames sweep through the inner Solar System at the left, linking up with gas giant Neptune, the Solar System's outermost planet, at the far right. Positions for Venus, Earth, Jupiter, Saturn, Uranus, and Neptune are indicated by letters, while the Sun is the bright spot near the center of the circle of frames. The inset frames for each of the planets are from Voyager's narrow field camera. Unseen in the portrait are Mercury, too close to the Sun to be detected, and Mars, unfortunately hidden by sunlight scattered in the camera's optical system. Closer to the Sun than Neptune at the time, small, faint Pluto's position was not covered.",
"Copyright": "Voyager Project,NASA",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 26,
"Title": "The Helix Nebula in Hydrogen and Oxygen",
"Poster": "https://apod.nasa.gov/apod/image/1902/Helix_Campbell_1585.jpg",
"Year": 2019,
"Month": 2,
"Day": 13,
"Explanation": "Is the Helix Nebula looking at you? No, not in any biological sense, but it does look quite like an eye. The Helix Nebula is so named because it also appears that you are looking down the axis of a helix. In actuality, it is now understood to have a surprisingly complex geometry, including radial filaments and extended outer loops. The Helix Nebula (aka NGC 7293) is one of brightest and closest examples of a planetary nebula, a gas cloud created at the end of the life of a Sun-like star. The remnant central stellar core, destined to become a white dwarf star, glows in light so energetic it causes the previously expelled gas to fluoresce. The featured picture, taken in the light emitted by oxygen (shown in blue) and hydrogen (shown in red), was created from 74 hours of exposure over three months from a small telescope in a backyard of suburban Melbourne, Australia. A close-up of the inner edge of the Helix Nebula shows complex gas knots of unknown origin.",
"Copyright": "Andrew Campbell",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 27,
"Title": "Plane Crossing a Crescent Moon",
"Poster": "https://apod.nasa.gov/apod/image/1902/PlaneTrailMoon_Staiger_1555.jpg",
"Year": 2019,
"Month": 2,
"Day": 12,
"Explanation": "No, this is not a good way to get to the Moon. What is pictured is a chance superposition of an airplane and the Moon. The contrail would normally appear white, but the large volume of air toward the setting Sun preferentially knocks away blue light, giving the reflected trail a bright red hue. Far in the distance, well behind the plane, is a crescent Moon, also slightly reddened. Captured a month ago above Valais, Switzerland, the featured image was taken so soon after sunset that planes in the sky were still in sunlight, as were their contrails. Within minutes, unfortunately, the impromptu sky show ended. The plane crossed the Moon and moved out of sight. The Moon set. The contrail became unilluminated and then dispersed.",
"Copyright": "Olivier Staiger(Binounistan.com)",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 28,
"Title": "New Data: Ultima Thule Surprisingly Flat",
"Poster": "https://apod.nasa.gov/apod/image/1902/MU69Flatter_NewHorizons_1920.jpg",
"Year": 2019,
"Month": 2,
"Day": 11,
"Explanation": "Ultima Thule is not the object humanity thought that it was last month. When the robotic New Horizons spacecraft zoomed past the distant asteroid Ultima Thule (officially 2014 MU69) in early January, early images showed two circular lobes that when most simply extrapolated to 3D were thought to be, roughly, spheres. However, analyses of newly beamed-back images -- including many taken soon after closest approach -- shows eclipsed stars re-appearing sooner than expected. The only explanation possible is that this 30-km long Kuiper belt object has a different 3D shape than believed only a few weeks ago. Specifically, as shown in the featured illustration, it now appears that the larger lobe -- Ultima -- is more similar to a fluffy pancake than a sphere, while the smaller lobe -- Thule -- resembles a dented walnut. The remaining uncertainty in the outlines are shown by the dashed blue lines. The new shape information indicates that gravity -- which contracts more massive bodies into spheres -- played perhaps less of a role in contouring the lobes of Ultima Thule than previously thought. The New Horizons spacecraft continued on to Ultima Thule after passing Pluto in mid-2015. New data and images are still being received.",
"Copyright": "NASA, JHU's APL, SwRI",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 29,
"Title": "Venus Unveiled",
"Poster": "https://apod.nasa.gov/apod/image/1902/VenusEarth_MagellanApollo17_3000.jpg",
"Year": 2019,
"Month": 2,
"Day": 10,
"Explanation": "What does Venus look like beneath its thick clouds? These clouds keep the planet's surface hidden from even the powerful telescopic eyes of Earth-bound astronomers. In the early 1990s, though, using imaging radar, NASA's Venus-orbiting Magellan spacecraft was able to lift the veil from the face of Venus and produced spectacular high resolution images of the planet's surface. Colors used in this computer generated picture of Magellan radar data are based on color images from the surface of Venus transmitted by the Soviet Venera 13 and 14 landers. The bright area running roughly across the middle represents the largest highland region of Venus known as Aphrodite Terra. Venus, on the left, is about the same size as our Earth, shown to the right for comparison.",
"Copyright": "NASA, JPL, Magellan Project, Apollo 17",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 30,
"Title": "Comet Iwamoto and the Sombrero Galaxy",
"Poster": "https://apod.nasa.gov/apod/image/1902/Iwamoto-104-2019griffin.jpg",
"Year": 2019,
"Month": 2,
"Day": 9,
"Explanation": "Comet Iwamoto (C/2018 Y1), shows off a pretty, greenish coma at the upper left in this telescopic field of view. Taken on February 4 from the Mount John Observatory, University of Canterbury, the 30 minute long total exposure time shows the comet sweeping quickly across a background of stars and distant galaxies in the constellation Virgo. The long exposure and Iwamoto's rapid motion relative to the stars and galaxies results in the noticeable blurred streak tracing the the comet's bright inner coma. In fact, the streaked coma gives the comet a remarkably similar appearance to Messier 104 at lower right, popularly known as the Sombrero Galaxy. The comet, a visitor to the inner Solar System, is a mere 4 light-minutes away though, while majestic Messier 104, a spiral galaxy posing edge-on, is 30 million light-years distant. The first binocular comet of 2019, Iwamoto will pass closest to Earth on February 12. This comet's highly elliptical orbit around the Sun stretches beyond the Kuiper belt with an estimated 1,371 year orbital period. That should bring it back to the inner Solar System in 3390 AD.",
"Copyright": "Ian Griffin (Otago Museum)",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 31,
"Title": "Moon, Four Planets, and Emu",
"Poster": "https://apod.nasa.gov/apod/image/1902/ACherney_MoonPlanets.jpg",
"Year": 2019,
"Month": 2,
"Day": 8,
"Explanation": "A luminous Milky Way falls toward the horizon in this deep skyscape, starting at the top of the frame from the stars of the Southern Cross and the dark Coalsack Nebula. Captured in the dark predawn of February 2nd from Central Victoria, Australia, planet Earth, the 26 day old waning crescent Moon still shines brightly near the horizon. The second and third brightest celestial beacons are Venus and Jupiter along the lower part of the Milky Way's central bulge. Almost in line with the brighter planets and Moon, Saturn is the pinprick of light just visible below and right of the lunar glow. Australia's first astronomers saw the elongated, bulging shape of the familiar Milky Way as a great celestial Emu. The Moon and planets could almost be the Emu's eggs on this starry night.",
"Copyright": "Alex Cherney(Terrastro,TWAN)",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 32,
"Title": "Fox Fur, Unicorn, and Christmas Tree",
"Poster": "https://apod.nasa.gov/apod/image/1902/FoxFur_new_color_2048px.jpg",
"Year": 2019,
"Month": 2,
"Day": 7,
"Explanation": "Clouds of glowing hydrogen gas fill this colorful skyscape in the faint but fanciful constellation Monoceros, the Unicorn. A star forming region cataloged as NGC 2264, the complex jumble of cosmic gas and dust is about 2,700 light-years distant and mixes reddish emission nebulae excited by energetic light from newborn stars with dark interstellar dust clouds. Where the otherwise obscuring dust clouds lie close to the hot, young stars they also reflect starlight, forming blue reflection nebulae. The telescopic image spans about 3/4 degree or nearly 1.5 full moons, covering 40 light-years at the distance of NGC 2264. Its cast of cosmic characters includes the the Fox Fur Nebula, whose dusty, convoluted pelt lies near the top, bright variable star S Monocerotis immersed in the blue-tinted haze near center, and the Cone Nebula pointing in from the right side of the frame. Of course, the stars of NGC 2264 are also known as the Christmas Tree star cluster. The triangular tree shape is seen on its side here. Traced by brighter stars it has its apex at the Cone Nebula. The tree's broader base is centered near S Monocerotis.",
"Copyright": "Stanislav Volskiy,Chilescope Team",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 33,
"Title": "Moon and Venus Appulse over a Tree",
"Poster": "https://apod.nasa.gov/apod/image/1902/MoonVenus_Dzierba_4386.jpg",
"Year": 2019,
"Month": 2,
"Day": 6,
"Explanation": "What's that bright spot near the Moon? Venus. About a week ago, Earth's Moon appeared unusually close to the distant planet Venus, an angular coincidence known as an appulse. Similar to a conjunction, which is a coordinate term, an appulse refers more generally to when two celestial objects appear close together. This Moon and Venus appulse -- once as close as 0.05 degrees -- was captured rising during the early morning behind Koko crater on the island of O'ahu in Hawaii, USA. The Moon was in a crescent phase with its lower left reflecting direct sunlight, while the rest of the Moon is seen because of Earthshine, sunlight first reflected from the Earth. Some leaves and branches of a foreground kiawe tree are seen in silhouette in front of the bright crescent, while others, in front of a darker background, appear white because of forward scattering. Appulses involving the Moon typically occur several times a year: for example the Moon is expected to pass within 0.20 degrees of distant Saturn on March 1.",
"Copyright": "Alex Dzierba",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 34,
"Title": "Perijove 16: Passing Jupiter",
"Poster": "https://apod.nasa.gov/apod/ap180226.html",
"Year": 2019,
"Month": 2,
"Day": 5,
"Explanation": "Watch Juno zoom past Jupiter again. NASA's robotic spacecraft Juno is continuing on its 53-day, highly-elongated orbits around our Solar System's largest planet. The featured video is from perijove 16, the sixteenth time that Juno has passed near Jupiter since it arrived in mid-2016. Each perijove passes near a slightly different part of Jupiter's cloud tops. This color-enhanced video has been digitally composed from 21 JunoCam still images, resulting in a 125-fold time-lapse. The video begins with Jupiter rising as Juno approaches from the north. As Juno reaches its closest view -- from about 3,500 kilometers over Jupiter's cloud tops -- the spacecraft captures the great planet in tremendous detail. Juno passes light zones and dark belt of clouds that circle the planet, as well as numerous swirling circular storms, many of which are larger than hurricanes on Earth. As Juno moves away, the remarkable dolphin-shaped cloud is visible. After the perijove, Jupiter recedes into the distance, now displaying the unusual clouds that appear over Jupiter's south. To get desired science data, Juno swoops so close to Jupiter that its instruments are exposed to very high levels of radiation.",
"Copyright": "The Planets, IV. Jupiter (Gustav Holst);USAF Heritage of America Band (via Wikipedia)",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 35,
"Title": "Henize 70: A Superbubble in the LMC",
"Poster": "https://apod.nasa.gov/apod/image/1902/N70_Durdis_2000.jpg",
"Year": 2019,
"Month": 2,
"Day": 4,
"Explanation": "Massive stars profoundly affect their galactic environments. Churning and mixing interstellar clouds of gas and dust, stars -- most notably those upwards of tens of times the mass of our Sun -- leave their mark on the compositions and locations of future generations of stars. Dramatic evidence of this is illustrated in our neighboring galaxy, the Large Magellanic Cloud (LMC), by the featured nebula, Henize 70 (also known as N70 and DEM301). Henize 70 is actually a luminous superbubble of interstellar gas about 300 light-years in diameter, blown by winds from hot, massive stars and supernova explosions, with its interior filled with tenuous hot and expanding gas. Because superbubbles can expand through an entire galaxy, they offer humanity a chance to explore the connection between the lifecycles of stars and the evolution of galaxies.",
"Copyright": "Josep M. Drudis",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 36,
"Title": "An Airglow Fan from Lake to Sky",
"Poster": "https://apod.nasa.gov/apod/image/1601/AirglowFan_Lane_2400.jpg",
"Year": 2019,
"Month": 2,
"Day": 3,
"Explanation": "Why would the sky look like a giant fan? Airglow. The featured intermittent green glow appeared to rise from a lake through the arch of our Milky Way Galaxy, as captured during 2015 next to Bryce Canyon in Utah, USA. The unusual pattern was created by atmospheric gravity waves, ripples of alternating air pressure that can grow with height as the air thins, in this case about 90 kilometers up. Unlike auroras powered by collisions with energetic charged particles and seen at high latitudes, airglow is due to chemiluminescence, the production of light in a chemical reaction. More typically seen near the horizon, airglow keeps the night sky from ever being completely dark.",
"Copyright": "Judy Schmidt",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 37,
"Title": "LDN 1622: Dark Nebula in Orion",
"Poster": "https://apod.nasa.gov/apod/image/1902/LDN1622_2019_01_14_1450min_LHaRGB.jpg",
"Year": 2019,
"Month": 2,
"Day": 2,
"Explanation": "The silhouette of an intriguing dark nebula inhabits this cosmic scene. Lynds' Dark Nebula (LDN) 1622 appears against a faint background of glowing hydrogen gas only easily seen in long telescopic exposures of the region. LDN 1622 lies near the plane of our Milky Way Galaxy, close on the sky to Barnard's Loop, a large cloud surrounding the rich complex of emission nebulae found in the Belt and Sword of Orion. But the obscuring dust of LDN 1622 is thought to be much closer than Orion's more famous nebulae, perhaps only 500 light-years away. At that distance, this 1 degree wide field of view would span less than 10 light-years. Its foreboding appearance lends this dark expanse a popular name, the Boogeyman Nebula.",
"Copyright": "Tapio Lahtinen",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
},
{
"Id": 38,
"Title": "Twin Galaxies in Virgo",
"Poster": "https://apod.nasa.gov/apod/image/1902/NGC4567_70chart32.jpg",
"Year": 2019,
"Month": 2,
"Day": 1,
"Explanation": "Spiral galaxy pair NGC 4567 and NGC 4568 share this sharp cosmic vista with lonely elliptical galaxy NGC 4564. All are members of the large Virgo Galaxy Cluster. With their classic spiral arms, dust lanes, and star clusters, the eye-catching spiral pair is also known as the Butterfly Galaxies or the Siamese Twins. Very close together, the galaxy twins don't seem to be too distorted by gravitational tides. Their giant molecular clouds are known to be colliding though and are likely fueling the formation of massive star clusters. The galaxy twins are about 52 million light-years distant, while their bright cores appear separated by about 20,000 light-years. Of course, the spiky foreground stars lie within our own Milky Way.",
"Copyright": "CHART32 Team,Processing - Johannes Schedler",
"PageAuthor": "Robert Nemiroff",
"PageEditor": "Jerry Bonnell"
}
]

current_id = 38

@app.route('/Add_item')
def additem():  
    return render_template('additem.html', data=data) 

@app.route('/Search')
def search():
    return render_template('search.html', data=data) 

@app.route('/Item/<id>')
def item(id=None):
    return render_template('items.html', id=id, data=data)

@app.route('/save_item', methods=['GET', 'POST'])
def save_item():
    global current_id
    global data

    json_data = request.get_json()
    title = json_data["Title"]
    link = json_data["Poster"]
    year = json_data["Year"]
    month = json_data["Month"]
    day = json_data["Day"]
    explanation = json_data["Explanation"]
    copyright = json_data["Copyright"]
    author = json_data["PageAuthor"]
    editor = json_data["PageEditor"]

    current_id += 1
    new_picture = {
        "Id":  current_id,
        "Title": title,
        "Poster": link,
        "Year": year,
        "Month": month,
        "Day": day,
        "Explanation": explanation,
        "Copyright": copyright,
        "PageAuthor": author,
        "PageEditor": editor
    }
    data.append(new_picture)

    return str(current_id)

@app.route('/search_item', methods=['GET', 'POST'])
def search_item():
    global current_id
    global data
    search_result = []

    keyword = request.get_json().lower()
    for i in range(current_id):
        item = data[i]
        con_year = str(item["Year"])
        con_month = str(item["Month"])
        con_day = str(item["Day"])
        if keyword in item["Title"].lower() or keyword in item["Explanation"].lower() or keyword in item["Copyright"].lower() or keyword in item["PageAuthor"].lower() or keyword in item["PageEditor"].lower() or keyword in con_year or keyword in con_month or keyword in con_day:
            search_result.append(item)

    search_result.sort(key=lambda x: datetime.datetime.strptime(str(x['Year']) + '-' + str(x['Month']) + '-' + str(x['Day']), '%Y-%m-%d'), reverse=True)

    return jsonify(search_result=search_result)

if __name__ == '__main__':
    app.run(debug = True)