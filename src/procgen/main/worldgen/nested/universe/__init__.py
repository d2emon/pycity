"""
universe stuff
"""
from ..factory import NestedFactory, NestedLocationFactory


# new Thing("multiverse", [UniverseFactory.multiple(10, 30)], ["multiverse", "lasagnaverse", "doughnutverse", "towelverse", "baconverse", "sharkverse", "nestedverse", "tastyverse", "upverse", "downverse", "layerverse", "clusterverse", "metaverse", "quantiverse", "paraverse", "epiverse", "alterverse", "hypoverse", "dimensioverse", "planiverse", "pluriverse", "polyverse", "maniverse", "stackoverse", "antiverse", "superverse", "upperverse", "maxiverse", "megaverse", "babyverse", "tinyverse", "retroverse", "ultraverse", "topoverse", "otherverse", "bubbleverse", "esreverse", "versiverse", "'verse", "cookieverse", "grandmaverse"]);


class TempFactory(NestedFactory):
    default_name = "temp"

    def child_factories(self):
        yield from []


class UniverseFactory(NestedLocationFactory):
    default_name = "universe"

    def child_factories(self):
        yield from SuperclusterFactory.multiple(10, 30)


class SuperclusterFactory(NestedLocationFactory):
    default_name = "galactic supercluster"

    def child_factories(self):
        yield from GalaxyFactory.multiple(10, 30)


class GalaxyFactory(NestedLocationFactory):
    default_name = "galaxy"

    def child_factories(self):
        yield from GalaxyCenter
        yield from GalaxyArm.multiple(2, 6)


class GalaxyArmFactory(NestedLocationFactory):
    default_name = "arm"

    def child_factories(self):
        # ["galactic life,5%", "dyson sphere,4%", "dyson sphere,2%", "star system,20-50", "nebula,0-12", "black hole,20%", "black hole,20%"]
        yield TempFactory


class GalaxyCenter(NestedLocationFactory):
    default_name = "galactic center"

    def child_factories(self):
        # ["black hole", "galactic life,10%", "dyson sphere,4%", "dyson sphere,2%", "star system,20-50", "nebula,0-12"]
        yield TempFactory


"""
new Thing("nebula",["galactic life,15%", "star,2%", "star,2%", "star,2%", "interstellar cloud,1-6"]);
new Thing("interstellar cloud",["helium", "hydrogen", "carbon,80%", "water,5%", "ammonia,5%", "nitrogen,5%", "iron,5%", "sulfur,5%", "oxygen,15%"],[["a bright pink", "a faint", "a fading", "a pale", "a fluo", "a glowing", "a green", "a bright green", "a dark brown", "a brooding", "a magenta", "a bright red", "a dark red", "a blueish", "a deep blue", "a turquoise", "a teal", "a golden", "a multicolored", "a silver", "a dramatic", "a luminous", "a colossal", "a purple", "a gold-trimmed", "an opaline", "a silvery", "a shimmering"], [" "], ["interstellar cloud"]]);
new Thing("star system",["star", "star,3%", "visitor planet,5%", "future planet,10%", "future planet,10%", "terraformed planet,50%", "terraformed planet,20%", "terraformed planet,10%", "medieval planet,30%", "medieval planet,20%", "ancient planet,50%", "ancient planet,30%", "ancient planet,10%", "barren planet,60%", "barren planet,40%", "barren planet,20%", "gas giant,60%", "gas giant,40%", "gas giant,20%", "gas giant,10%", "asteroid belt,0-2"]);
new Thing("dyson sphere",["star", "star,3%", "dyson surface", "future planet,1-8", "barren planet,60%", "barren planet,40%", "barren planet,20%", "gas giant,60%", "gas giant,40%", "gas giant,20%", "gas giant,10%", "asteroid belt,0-2"]);
new Thing("star",["ghost,0.1%", "space monster,0.2%", "hydrogen", "helium"],[["white", "faint", "yellow", "red", "blue", "green", "purple", "bright", "double", "twin", "triple", "old", "young", "dying", "small", "giant", "large", "pale", "dark", "hell", "horrific", "twisted", "spectral"], [" star"]]);
new Thing("planet",[".terraformed planet"],"telluric planet");
new Thing("barren planet",["galactic life,10%", "rock", "ice,50%", ".planet composition"],"telluric planet");
new Thing("visitor planet",["visitor city,1-8", "visitor installation,2-6", "galactic life", "rock", "ice,50%", ".planet composition"],"telluric planet");
new Thing("future planet",["future continent,2-7", "ocean,1-7", "future sky", ".future moon,30%", ".planet composition"],"telluric planet");
new Thing("terraformed planet",["continent,2-7", "ocean,1-7", "terraformed sky", ".terraformed moon,30%", ".planet composition"],"telluric planet");
new Thing("medieval planet",["medieval continent,2-4", "ancient continent,0-3", "ocean,1-7", "sky", ".planet composition"],"telluric planet");
new Thing("ancient planet",["ancient continent,2-7", "ocean,1-7", "sky", ".planet composition"],"telluric planet");
new Thing("planet composition",["planet core", "moon,40%", "moon,20%", "moon,10%"],"planet");
new Thing("moon",["ghost,0.1%", "rock", "planet core"],[["young", "old", "large", "small", "pale", "white", "dark", "black", "old"], [" moon"]]);
new Thing("terraformed moon",[".planet composition", "continent,1-4", "ocean,1-4", "sky"],[["young", "old", "large", "small", "pale", "white", "dark", "black", "old", "green", "lush", "blue", "city", "colonized", "life"], [" moon"]]);
new Thing("asteroid belt",["galactic life,20%", "asteroid,10-30"]);
new Thing("earth",[".asteroid belt"],"Earth");
new Thing("asteroid",["space animal,0.5%", "rock", "ice,30%"],"asteroid");
new Thing("gas giant",["gas giant atmosphere", "planet core,50%", "moon,0-3", "terraformed moon,20%", "terraformed moon,10%"]);
new Thing("gas giant atmosphere",["galactic life,10%", "helium", "hydrogen", "water,50%", "ammonia,50%", "methane,50%"],"atmosphere");
new Thing("planet core",["space monster,0.5%", "iron", "rock", "diamond,2%", "magma"],"core");

new Thing("black hole",["inside the black hole"]);
new Thing("inside the black hole",["end of universe note,0.5%", "crustacean,0.2%", "white hole"]);
new Thing("white hole",[UniverseFactory]);
new Thing("42",[UniverseFactory]);
new Thing("everything",[UniverseFactory]);
new Thing("end of universe note",["pasta,0.1%"],["Help! I'm trapped in a universe factory!", "Okay, you can stop clicking now.", "I want to get off Mr Orteil's Wild Ride", "my sides"]);
new Thing("orteil",["body", "orteil psyche", "clothing set", "computer"],"Orteil");
//I do what I want
new Thing("god",[".orteil"],"Orteil");
//I'm a fucking god
new Thing("orteil psyche",["orteil thoughts"],"psyche");
new Thing("orteil thoughts",[],["OH MY GOD WHAT ARE YOU DOING HERE TURN BACK IMMEDIATELY", "WHAT IS WRONG WITH YOU", "WHAT THE HELL GO AWAY", "WHAT ARE YOU DOING OH GOD", "WHY THE HELL ARE YOU HERE", "I DO WHAT I WANT OKAY", "NO I DON'T CARE GO AWAY", "WHAT DID I EVEN DO TO YOU", "OH NO WHY THIS", "OKAY JUST <a href=\"http://orteil.deviantart.com\">GO THERE ALREADY</a>", "<a href=\"http://twitter.com/orteil42\">WHATEVER</a>"]);
"""
