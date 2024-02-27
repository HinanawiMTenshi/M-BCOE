#coding=utf-8
# -*- coding: cp1254 -*-

from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *

####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################

# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile   = imodbit_bent | imodbit_large_bag
imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent
# Replace winged mace/spiked mace with: Flanged mace / Knobbed mace?
# Fauchard (majowski glaive) 
items = [
# item_name, mesh_name, item_properties, item_capabilities, slot_no, cost, bonus_flags, weapon_flags, scale, view_dir, pos_offset
 ["no_item","INVALID ITEM", [("invalid_item",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],

#************************************************************************************************
# ITEMS before this point are hardcoded into item_codes.h and their order should not be changed!
#************************************************************************************************


####################
## MM ITEMS Begin ##
####################
#Weapons

# Pistols
 # French
["french_cav_pistol", "Pistol", [("french_cav_pistol",0)], itp_type_pistol|itp_merchandise|itp_primary|itp_cant_reload_while_moving_mounted ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_revolver_right , 230 , weight(1.5)|difficulty(0)|spd_rtng(30) | shoot_speed(200) | thrust_damage(60 ,pierce)|max_ammo(1)|accuracy(25),imodbits_none, #patch1115 27/1 begin
 []],
#[(ti_on_weapon_attack, [(store_trigger_param_1,":user_agent"),(call_script, "script_server_fire_musket", ":user_agent", firearm_type_pistol)])]],
["french_officer_pistol", "Pistol", [("french_officer_pistol",0)], itp_type_pistol|itp_merchandise|itp_primary|itp_cant_reload_while_moving_mounted ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_revolver_right , 230 , weight(1.5)|difficulty(0)|spd_rtng(30) | shoot_speed(200) | thrust_damage(60 ,pierce)|max_ammo(1)|accuracy(25),imodbits_none,
 []],
#[(ti_on_weapon_attack, [(store_trigger_param_1,":user_agent"),(call_script, "script_server_fire_musket", ":user_agent", firearm_type_pistol)])]],
["french_pistol_1766", "Pistol", [("french_pistol_1766",0)], itp_type_pistol|itp_merchandise|itp_primary|itp_cant_reload_while_moving_mounted ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_revolver_right , 230 , weight(1.5)|difficulty(0)|spd_rtng(30) | shoot_speed(200) | thrust_damage(60 ,pierce)|max_ammo(1)|accuracy(25),imodbits_none,
 []],
#[(ti_on_weapon_attack, [(store_trigger_param_1,":user_agent"),(call_script, "script_server_fire_musket", ":user_agent", firearm_type_pistol)])]],
["french_pistol_1777", "Pistol", [("french_pistol_1777",0)], itp_type_pistol|itp_merchandise|itp_primary|itp_cant_reload_while_moving_mounted ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_revolver_right , 230 , weight(1.5)|difficulty(0)|spd_rtng(30) | shoot_speed(200) | thrust_damage(60 ,pierce)|max_ammo(1)|accuracy(25),imodbits_none,
 []],
#[(ti_on_weapon_attack, [(store_trigger_param_1,":user_agent"),(call_script, "script_server_fire_musket", ":user_agent", firearm_type_pistol)])]],

 # Russian
["russian_pistol", "Pistol", [("Russian_pistol",0)], itp_type_pistol|itp_merchandise|itp_primary|itp_cant_reload_while_moving_mounted ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_revolver_right , 230 , weight(1.5)|difficulty(0)|spd_rtng(30) | shoot_speed(200) | thrust_damage(60 ,pierce)|max_ammo(1)|accuracy(25),imodbits_none,
 []],
#[(ti_on_weapon_attack, [(store_trigger_param_1,":user_agent"),(call_script, "script_server_fire_musket", ":user_agent", firearm_type_pistol)])]],

 # British
 
["british_pistol", "Pistol", [("new_land_pattern_pistol",0)], itp_type_pistol|itp_merchandise|itp_primary|itp_cant_reload_while_moving_mounted ,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_revolver_right , 
230 , weight(1.5)|difficulty(0)|spd_rtng(30) | shoot_speed(200) | thrust_damage(60 ,pierce)|max_ammo(1)|accuracy(25),imodbits_none, #patch1115 27/1 begin
 []],

 
# Carabines
# French
["french_mousquiton", "Tepo", [("dou_tanegashima",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(20) | shoot_speed(250) | thrust_damage(120 ,pierce)|max_ammo(1)|accuracy(65),imodbits_none,[]],
["french_mousquiton_melee", "Tepo", [("dou_tanegashima",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(86) | weapon_length(104)|swing_damage(23 , blunt) | thrust_damage(12,  blunt),imodbits_none ],
["french_mousquiton_ai", "Cavalry Carbine", [("french_mousquiton",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(27) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(65),imodbits_none,[]],

["nanban_biggun", "Nanban biggun", [("nmtong",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(15) | shoot_speed(250) | thrust_damage(150 ,pierce)|max_ammo(1)|accuracy(65),imodbits_none,[]],
["nanban_biggun_melee", "Nanban biggun", [("nmtong",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(100) | weapon_length(104)|swing_damage(23 , blunt) | thrust_damage(12,  blunt),imodbits_none ],

["nanban_matchlock", "Nanban matchlock", [("arquebus",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(16) | shoot_speed(250) | thrust_damage(120 ,pierce)|max_ammo(1)|accuracy(70),imodbits_none,[]],
["nanban_matchlock_melee", "Nanban matchlock", [("arquebus",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(86) | weapon_length(104)|swing_damage(23 , blunt) | thrust_damage(12,  blunt),imodbits_none ],

["nanban_matchlock2", "Nanban matchlock", [("matchlock_1",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(16) | shoot_speed(250) | thrust_damage(120 ,pierce)|max_ammo(1)|accuracy(70),imodbits_none,[]],
["nanban_matchlock2_melee", "Nanban matchlock", [("matchlock_1",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(86) | weapon_length(104)|swing_damage(23 , blunt) | thrust_damage(12,  blunt),imodbits_none ],


["tepo", "Tepo", [("tiepao",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(23) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(60),imodbits_none,[]],
["tepo_melee", "Tepo", [("tiepao",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(86) | weapon_length(95)|swing_damage(23 , blunt) | thrust_damage(12,  blunt),imodbits_none ],

["french_mousquiton_light", "Light Cavalry Tepo", [("french_mousquiton_light",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(27) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(65),imodbits_none,[]],
["french_mousquiton_light_melee", "Light Cavalry Tepo", [("french_mousquiton_light",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(86) | weapon_length(76)|swing_damage(23 , blunt) | thrust_damage(12,  blunt),imodbits_none ],
["french_mousquiton_light_ai", "Light Cavalry Carbine", [("french_mousquiton_light",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(27) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(65),imodbits_none,[]],

["french_dragoon_musket", "Cavalry Musket", [("french_dragoon_musket",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(25) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(72),imodbits_none,[]],
["french_dragoon_musket_melee", "Cavalry Musket", [("french_dragoon_musket",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(86) | weapon_length(115)|swing_damage(20 , blunt) | thrust_damage(12,  blunt),imodbits_none ],#patch1115 48/1
["french_dragoon_musket_ai", "Cavalry Musket", [("french_dragoon_musket",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(25) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(72),imodbits_none,[]],

["xunleichong", "Ming multi-barrel handgonne", [("Xunlei",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_use_on_horseback|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_throw_knife|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(10) | shoot_speed(250) | thrust_damage(60 ,pierce)|max_ammo(12)|accuracy(60),imodbits_none,[]],
["xunleichong_melee", "Cavalry Musket", [("Xunlei",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket,itc_lance|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(86) | weapon_length(75)|swing_damage(20 , blunt) | thrust_damage(30,  pierce),imodbits_none ],#patch1115 48/1

["gatling", "Gatling machinegun", [("gatling",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_use_on_horseback|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(65) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(100)|accuracy(120),imodbits_none,[]],


["short_tepo1", "Light Cavalry Tepo1", [("tiepao2",0),("tiepao2_carry", ixmesh_carry)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_spear, 
683 , weight(3.0)|difficulty(0)|spd_rtng(24) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(55),imodbits_none,[]],
["short_tepo1_melee", "Light Cavalry Tepo", [("tiepao2",0),("tiepao2_carry", ixmesh_carry)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket,itc_musket_melee|itcf_carry_spear,
180 , weight(0)|difficulty(0)|spd_rtng(86) | weapon_length(65)|swing_damage(23 , blunt) | thrust_damage(12,  blunt),imodbits_none ],

["short_tepo1_ai", "Light Cavalry Tepo1", [("tiepao2",0),("tiepao2_carry", ixmesh_carry)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_spear, 
683 , weight(3.0)|difficulty(0)|spd_rtng(24) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(55),imodbits_none,[]],

["short_tepo2", "Light Cavalry Tepo2", [("mstong",0),("mstong_carry", ixmesh_carry)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_spear, 
683 , weight(3.0)|difficulty(0)|spd_rtng(24) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(55),imodbits_none,[]],
["short_tepo2_melee", "Light Cavalry Tepo", [("mstong",0),("mstong_carry", ixmesh_carry)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket,itc_musket_melee|itcf_carry_spear,
180 , weight(0)|difficulty(0)|spd_rtng(86) | weapon_length(65)|swing_damage(23 , blunt) | thrust_damage(12,  blunt),imodbits_none ],

["short_tepo2_ai", "Light Cavalry Tepo2", [("mstong",0),("mstong_carry", ixmesh_carry)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_spear, 
683 , weight(3.0)|difficulty(0)|spd_rtng(24) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(55),imodbits_none,[]],

["short_niaochong", "Light Cavalry Niaochong", [("short_niaochong",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_spear, 
683 , weight(3.0)|difficulty(0)|spd_rtng(22) | shoot_speed(250) | thrust_damage(90 ,pierce)|max_ammo(1)|accuracy(57),imodbits_none,[]],
["short_niaochong_melee", "Light Cavalry Niaochong", [("short_niaochong",0),("mstong_carry", ixmesh_carry)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket,itc_musket_melee|itcf_carry_spear,
180 , weight(0)|difficulty(0)|spd_rtng(86) | weapon_length(65)|swing_damage(23 , blunt) | thrust_damage(12,  blunt),imodbits_none ],

["short_niaochong_ai", "Light Cavalry Niaochong", [("short_niaochong",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_spear, 
683 , weight(3.0)|difficulty(0)|spd_rtng(22) | shoot_speed(250) | thrust_damage(90 ,pierce)|max_ammo(1)|accuracy(57),imodbits_none,[]],

["naginata1", "Naginata", [("gekokujo_naginata_6",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_guandao2,
 180 , weight(3.5)|difficulty(0)|spd_rtng(85) | weapon_length(239)|swing_damage(45 ,  cut) | thrust_damage(35 ,  pierce),imodbits_polearm ],
 
["naginata2", "Naginata", [("gekokujo_naginata_5",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_guandao2,
 180 , weight(3.5)|difficulty(0)|spd_rtng(98) | weapon_length(147)|swing_damage(42 ,  cut) | thrust_damage(32 ,  pierce),imodbits_polearm ],

# Russian
["russian_dragoon_musket", "Cavalry Musket", [("Russian_dragoon_musket",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(25) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(72),imodbits_none,[]],
# [(ti_on_weapon_attack, [(store_trigger_param_1,":user_agent"),(call_script, "script_server_fire_musket", ":user_agent", firearm_type_carabine)])]],
["russian_dragoon_musket_melee", "Cavalry Musket", [("Russian_dragoon_musket",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(86) | weapon_length(115)|swing_damage(20 , blunt) | thrust_damage(12,  blunt),imodbits_none ],
["russian_dragoon_musket_ai", "Cavalry Musket", [("Russian_dragoon_musket",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(25) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(72),imodbits_none,[]],

["russian_cavalry_stutzer_1803", "Short Carbine", [("Russian_cavalry_stutzer_1803",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving|itp_cant_reload_while_moving_mounted ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(29) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(40),imodbits_none,[]],
# [(ti_on_weapon_attack, [(store_trigger_param_1,":user_agent"),(call_script, "script_server_fire_musket", ":user_agent", firearm_type_carabine)])]],
["russian_gusarskiy_karabin", "Musketoon", [("garlacz_a",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(18) | shoot_speed(180) | thrust_damage(70 ,pierce)|max_ammo(1)|accuracy(54),imodbits_none,
 [(ti_on_weapon_attack, [
  (this_or_next|multiplayer_is_server),
  (neg|game_in_multiplayer_mode),
  (store_trigger_param_1,":agent_id"),
  (eq,":agent_id",":agent_id"), # fix compiler bug warning.
  (copy_position,pos22,pos1),
  (position_move_y,pos22,110),
  (try_for_range,":unused",0,4), #4 extra bullets + 1 original = 5 bullets in one shot :D
    (copy_position,pos23,pos22),
    (store_random_in_range,":x_change",-15,16),
    (store_random_in_range,":z_change",-15,16),
    (position_rotate_x, pos23, ":x_change"),
    (position_rotate_z, pos23, ":z_change"),
    (set_fixed_point_multiplier,100),
    (store_random_in_range,":bullet_speed",12000,16000),
    (add_missile, ":agent_id", pos23, ":bullet_speed", "itm_cannon_canister_dummy", 0, "itm_canister_ammo", 0),
  (try_end),
  ])]],
["russian_gusarskiy_karabin_melee", "Musketoon", [("garlacz_a",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(86) | weapon_length(58)|swing_damage(22 , blunt) | thrust_damage(12,  blunt),imodbits_none ],
["russian_gusarskiy_karabin_ai", "Musketoon", [("garlacz_a",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(18) | shoot_speed(180) | thrust_damage(70 ,pierce)|max_ammo(1)|accuracy(54),imodbits_none,
 [(ti_on_weapon_attack, [
  (this_or_next|multiplayer_is_server),
  (neg|game_in_multiplayer_mode),
  (store_trigger_param_1,":agent_id"),
  (eq,":agent_id",":agent_id"), # fix compiler bug warning.
  (copy_position,pos22,pos1),
  (position_move_y,pos22,110),
  (try_for_range,":unused",0,4), #4 extra bullets + 1 original = 5 bullets in one shot :D
    (copy_position,pos23,pos22),
    (store_random_in_range,":x_change",-15,16),
    (store_random_in_range,":z_change",-15,16),
    (position_rotate_x, pos23, ":x_change"),
    (position_rotate_z, pos23, ":z_change"),
    (set_fixed_point_multiplier,100),
    (store_random_in_range,":bullet_speed",12000,16000),
    (add_missile, ":agent_id", pos23, ":bullet_speed", "itm_cannon_canister_dummy", 0, "itm_canister_ammo", 0),
  (try_end),
  ])]],

# British
["british_carbine", "Cavalry Carbine", [("paget_carabine",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(27) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(65),imodbits_none,[]],
["british_carbine_melee", "Cavalry Carbine", [("paget_carabine",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(86) | weapon_length(50)|swing_damage(23 , blunt) | thrust_damage(12,  blunt),imodbits_none ],
["british_carbine_ai", "Cavalry Carbine", [("paget_carabine",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(27) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(65),imodbits_none,[]],

# Rifles
# Russian
["russian_rifle_1805", "Rifle", [("Russian_rifle_1805",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(18) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(87),imodbits_none,[]],
# [(ti_on_weapon_attack, [(store_trigger_param_1,":user_agent"),(call_script, "script_server_fire_musket", ":user_agent", firearm_type_rifle)])]],
["russian_rifle_1805_melee", "Rifle", [("Russian_rifle_1805",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket|itp_can_knock_down,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(74)|swing_damage(23 , blunt) | thrust_damage(22 ,  blunt),imodbits_none ],

# Matchlock
["british_baker_rifle", "Asia Matchlock", [("niaochong",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.75)|difficulty(0)|spd_rtng(20) | shoot_speed(250) | thrust_damage(120 ,pierce)|max_ammo(1)|accuracy(65),imodbits_none,[]],
# [(ti_on_weapon_attack, [(store_trigger_param_1,":user_agent"),(call_script, "script_server_fire_musket", ":user_agent", firearm_type_rifle)])]],
["british_baker_rifle_melee", "Asia Matchlock", [("niaochong",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket|itp_can_knock_down,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(135)|swing_damage(23 , blunt) | thrust_damage(22 ,  blunt),imodbits_none ],

["whellock_pistol", "Whellock Pistol", [("whellock_pistol",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left,
683 , weight(3.75)|difficulty(0)|spd_rtng(30) | shoot_speed(250) | thrust_damage(65 ,pierce)|max_ammo(1)|accuracy(30),imodbits_none,[]],

["whellock_pistol2", "Whellock Pistol", [("pistol_pure_b",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left,
683 , weight(3.75)|difficulty(0)|spd_rtng(30) | shoot_speed(250) | thrust_damage(65 ,pierce)|max_ammo(1)|accuracy(30),imodbits_none,[]],

["whellock_pistol_pure", "Whellock Pistol", [("pistol_rich_a",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left,
683 , weight(3.75)|difficulty(0)|spd_rtng(30) | shoot_speed(250) | thrust_damage(75 ,pierce)|max_ammo(1)|accuracy(45),imodbits_none,[]],

["flintlock_pistol", "Flintlock Pistol", [("pistol_firelock_long",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left,
683 , weight(3.75)|difficulty(0)|spd_rtng(30) | shoot_speed(250) | thrust_damage(65 ,pierce)|max_ammo(1)|accuracy(30),imodbits_none,[]],

["matchlockpistol", "Matchlock Pistol", [("fuse_lock_pistol",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted,itcf_shoot_pistol|itcf_reload_pistol|itcf_carry_pistol_front_left,
683 , weight(3.75)|difficulty(0)|spd_rtng(26) | shoot_speed(250) | thrust_damage(60 ,pierce)|max_ammo(1)|accuracy(25),imodbits_none,[]],

["qingmatchlock", "Qing Matchlock", [("huoqiang",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(4.00)|difficulty(0)|spd_rtng(18) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(65),imodbits_none,[]],
# [(ti_on_weapon_attack, [(store_trigger_param_1,":user_agent"),(call_script, "script_server_fire_musket", ":user_agent", firearm_type_rifle)])]],
["qingmatchlock_melee", "Qing Matchlock", [("huoqiang",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket|itp_can_knock_down,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(150)|swing_damage(23 , blunt) | thrust_damage(22 ,  blunt),imodbits_none ],

["qingmatchlock2", "Qing Matchlock", [("qing_niaoqiang2",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(4.00)|difficulty(0)|spd_rtng(15) | shoot_speed(250) | thrust_damage(120 ,pierce)|max_ammo(1)|accuracy(70),imodbits_none,[]],
# [(ti_on_weapon_attack, [(store_trigger_param_1,":user_agent"),(call_script, "script_server_fire_musket", ":user_agent", firearm_type_rifle)])]],
["qingmatchlock2_melee", "Qing Matchlock", [("qing_niaoqiang2",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket|itp_can_knock_down,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(140)|swing_damage(23 , blunt) | thrust_damage(22 ,  blunt),imodbits_none ],

["mingturkeymusket", "Lumi musket", [("1Ming_qiang",0)], itp_cant_use_on_horseback|itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.5)|difficulty(0)|spd_rtng(15) | shoot_speed(250) | thrust_damage(150 ,pierce)|max_ammo(1)|accuracy(70),imodbits_none,[]],

["mingturkeymusket_melee", "Lumi musket", [("1Ming_qiang",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket|itp_can_knock_down,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(135)|swing_damage(23 , blunt) | thrust_damage(22 ,  blunt),imodbits_none ],

["light_matchlock", "Light Matchlock", [("fuselock_petrynal",0)], itp_cant_use_on_horseback|itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.5)|difficulty(0)|spd_rtng(20) | shoot_speed(250) | thrust_damage(125 ,pierce)|max_ammo(1)|accuracy(65),imodbits_none,[]],

["light_matchlock_melee", "Light Matchlock", [("fuselock_petrynal",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket|itp_can_knock_down,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(105)|swing_damage(23 , blunt) | thrust_damage(22 ,  blunt),imodbits_none ],

["turkish_musket", "Turkish Matchlock", [("turkish_musket_a",0)], itp_cant_use_on_horseback|itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.5)|difficulty(0)|spd_rtng(20) | shoot_speed(250) | thrust_damage(125 ,pierce)|max_ammo(1)|accuracy(65),imodbits_none,[]],

["turkish_musket_melee", "Turkish Matchlock", [("turkish_musket_a",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket|itp_can_knock_down,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(105)|swing_damage(23 , blunt) | thrust_damage(22 ,  blunt),imodbits_none ],

["arbian_musket", "Arbian Matchlock", [("musket_turk_fitil_pure_huosheng",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving|itp_cant_reload_while_moving_mounted|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.5)|difficulty(0)|spd_rtng(20) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(60),imodbits_none,[]],

["arbian_musket_melee", "Arbian Matchlock", [("musket_turk_fitil_pure_huosheng",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket|itp_can_knock_down,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(125)|swing_damage(23 , blunt) | thrust_damage(22 ,  blunt),imodbits_none ],

["heavy_matchlock", "Heavy matchlock", [("mat1mele",0)], itp_cant_use_on_horseback|itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
683 , weight(3.5)|difficulty(0)|spd_rtng(15) | shoot_speed(250) | thrust_damage(180 ,pierce)|max_ammo(1)|accuracy(80),imodbits_none,[]],

["heavy_matchlock_melee", "Heavy matchlock", [("mat1mele",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket|itp_can_knock_down,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(125)|swing_damage(23 , blunt) | thrust_damage(22 ,  blunt),imodbits_none ],

["heavy_matchlock2", "Heavy matchlock", [("mat1mele",0)], itp_cant_use_on_horseback|itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
683 , weight(3.5)|difficulty(0)|spd_rtng(15) | shoot_speed(250) | thrust_damage(180 ,pierce)|max_ammo(1)|accuracy(80),imodbits_none,[]],

["heavy_matchlock_melee2", "Heavy matchlock", [("mat1mele",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket|itp_can_knock_down,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(125)|swing_damage(23 , blunt) | thrust_damage(22 ,  blunt),imodbits_none ],

["pishaw_musket", "Pishal musket", [("mat1mele",0)], itp_cant_use_on_horseback|itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_crossbow|itcf_carry_crossbow_back, 
683 , weight(3.5)|difficulty(0)|spd_rtng(15) | shoot_speed(250) | thrust_damage(220 ,pierce)|max_ammo(1)|accuracy(80),imodbits_none,[]],

["pishaw_musket_melee", "Pishal musket", [("mat1mele",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket|itp_can_knock_down,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(125)|swing_damage(23 , blunt) | thrust_damage(22 ,  blunt),imodbits_none ],#guchen


["light_whellock", "Light Whellock", [("wheellock_long",0)],itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.5)|difficulty(0)|spd_rtng(25) | shoot_speed(250) | thrust_damage(105 ,pierce)|max_ammo(1)|accuracy(75),imodbits_none,[]],

["light_whellock_melee", "Light Whellock", [("wheellock_long",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket|itp_can_knock_down,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(125)|swing_damage(23 , blunt) | thrust_damage(22 ,  blunt),imodbits_none ],

["light_flintlock", "Light flintlock", [("snaphans_musket",0)], itp_cant_use_on_horseback|itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.5)|difficulty(0)|spd_rtng(20) | shoot_speed(250) | thrust_damage(125 ,pierce)|max_ammo(1)|accuracy(65),imodbits_none,[]],

["light_flintlock_melee", "Light flintlock", [("snaphans_musket",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket|itp_can_knock_down,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(125)|swing_damage(23 , blunt) | thrust_damage(22 ,  blunt),imodbits_none ],

["russian_flintlock", "Light flintlock", [("snaphans_musket",0)], itp_cant_use_on_horseback|itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.5)|difficulty(0)|spd_rtng(20) | shoot_speed(250) | thrust_damage(110 ,pierce)|max_ammo(1)|accuracy(75),imodbits_none,[]],

["russian_flintlock_melee", "Light flintlock", [("snaphans_musket",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket|itp_can_knock_down,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(125)|swing_damage(23 , blunt) | thrust_damage(22 ,  blunt),imodbits_none ],

["flintlock_cabine", "Flintlock Cabine", [("firelock_regular_short",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving|itp_cant_reload_while_moving_mounted|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.5)|difficulty(0)|spd_rtng(22) | shoot_speed(250) | thrust_damage(125 ,pierce)|max_ammo(1)|accuracy(60),imodbits_none,[]],

["flintlock_cabine_melee", "Flintlock Cabine", [("firelock_regular_short",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket|itp_can_knock_down,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(95)|swing_damage(23 , blunt) | thrust_damage(22 ,  blunt),imodbits_none ],

["flintlock_cabine_ai", "Flintlock Cabine", [("firelock_regular_short",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving|itp_cant_reload_while_moving_mounted|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.5)|difficulty(0)|spd_rtng(22) | shoot_speed(250) | thrust_damage(125 ,pierce)|max_ammo(1)|accuracy(60),imodbits_none,[]],

["whellock_cabine", "Whellock Cabine", [("wheellock_carbine_1",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving|itp_cant_reload_while_moving_mounted|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.5)|difficulty(0)|spd_rtng(25) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(55),imodbits_none,[]],

["whellock_cabine_melee", "Whellock Cabine", [("wheellock_carbine_1",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket|itp_can_knock_down,itc_musket_melee|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(85)|swing_damage(23 , blunt) | thrust_damage(22 ,  blunt),imodbits_none ],

["whellock_cabine_ai", "Whellock Cabine", [("wheellock_carbine_1",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving|itp_cant_reload_while_moving_mounted|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.5)|difficulty(0)|spd_rtng(25) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(55),imodbits_none,[]],

#Yumi
["yumi1", "Yumi", [("gekokujo_yumi_6", 0), ("gekokujo_yumi_6_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 
594, weight(1.5)|difficulty(0)|spd_rtng(67)|shoot_speed(65)|abundance(100)|thrust_damage(15, pierce)|max_ammo(0), imodbits_bow, [] ],
 
["yumi2", "War_Yumi", [("Douran_Yumi2", 0), ("Douran_Yumi2_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 
862, weight(1.75)|difficulty(0)|spd_rtng(61)|shoot_speed(50)|abundance(100)|thrust_damage(20, pierce)|max_ammo(0), imodbits_bow, [] ],

["yumi_spear", "Yumi with spear", [("mtgong", 0)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 
862, weight(2.00)|difficulty(0)|spd_rtng(61)|shoot_speed(55)|abundance(100)|thrust_damage(22, cut)|max_ammo(0), imodbits_bow, [] ],


["katana_6","Katana", [("ggekokujo_katana_1", 0), ("ggekokujo_katana_1_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_katana|itcf_show_holster_when_drawn, 
210 , weight(2)|difficulty(0)|spd_rtng(105) | weapon_length(89)|swing_damage(40 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],

["katana_7","Katana", [("ggekokujo_katana_7", 0), ("ggekokujo_katana_7_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_katana|itcf_show_holster_when_drawn, 
210 , weight(2)|difficulty(0)|spd_rtng(105) | weapon_length(78)|swing_damage(40 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],



#Cheat
["sniper_rifle", "Sniper Rifle", [("Russian_rifle_1805",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_musket|itcf_reload_pistol|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(300) | shoot_speed(250) | thrust_damage(300 ,pierce)|max_ammo(40)|accuracy(100),imodbits_none,[]],
# [(ti_on_weapon_attack, [(store_trigger_param_1,":user_agent"),(call_script, "script_server_fire_musket", ":user_agent", firearm_type_rifle)])]],
["blunderbluss", "Blunderbluss", [("Russian_gusarskiy_karabin",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(150) | shoot_speed(200) | thrust_damage(300 ,pierce)|max_ammo(1)|accuracy(75),imodbits_none,
 [(ti_on_weapon_attack, [
  (this_or_next|multiplayer_is_server),
  (neg|game_in_multiplayer_mode),
  (store_trigger_param_1,":agent_id"),
  (eq,":agent_id",":agent_id"), # fix compiler bug warning.
  (copy_position,pos22,pos1),
  (position_move_y,pos22,110),
  (try_for_range,":unused",0,29), #29 extra bullets + 1 original = 20 bullets in one shot :D #mathishard
    (copy_position,pos23,pos22),
    (store_random_in_range,":x_change",-7,8),
    (store_random_in_range,":z_change",-10,11),
    (position_rotate_x, pos23, ":x_change"),
    (position_rotate_z, pos23, ":z_change"),
    (set_fixed_point_multiplier,100),
    (store_random_in_range,":bullet_speed",12000,19000),
    (add_missile, ":agent_id", pos23, ":bullet_speed", "itm_cannon_canister_dummy", 0, "itm_canister_ammo", 0),
  (try_end),
  ])]],
  
  ["sniper_rifle_ball", "Sniper Rifle", [("Russian_rifle_1805",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_musket|itcf_reload_pistol|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(300) | shoot_speed(250) | thrust_damage(300 ,pierce)|max_ammo(40)|accuracy(100),imodbits_none,
 [(ti_on_weapon_attack, [
  (this_or_next|multiplayer_is_server),
  (neg|game_in_multiplayer_mode),
  (store_trigger_param_1,":agent_id"),
  (eq,":agent_id",":agent_id"), # fix compiler bug warning.
  
   (set_fixed_point_multiplier, 100),
   (init_position,pos9), # pos9 holds new pos for cannonball
   (position_copy_origin,pos9,pos1),
   (position_get_rotation_around_x,":x_rot",pos1),
   (position_get_rotation_around_z,":z_rot",pos1),
   
   
   (val_add,":z_rot",90),
   (assign,":y_rot",":x_rot"),
   (try_begin),
     (gt,":y_rot",179),
     (val_sub,":y_rot",360),
   (try_end),
   (val_mul,":y_rot",-1),
   
   (position_rotate_z,pos9,":z_rot"),
   
   (assign,":init_vel",45), # 45 meters per 0.5 seconds = 90m/s
   (assign,":ammo_size","spr_mm_cannonball_code_only_12pd"),
   (assign,":flight_sound_id","snd_cannonball_loop"),
 
   (set_fixed_point_multiplier, 1000),
   # make rotation fixed point.
   (val_mul,":y_rot",1000),
   
   # x += Speed * Math.Cos(angle);
   (store_cos, ":cos_of_angle", ":y_rot"),
   (store_mul,":init_x_vel",":cos_of_angle",":init_vel"),
   (val_div,":init_x_vel",10),
   
   # z += speed * Math.Sin(angle);
   (store_sin, ":sin_of_angle", ":y_rot"),
   (store_mul,":init_z_vel",":sin_of_angle",":init_vel"),
   (val_div,":init_z_vel",10),
   (val_mul,":init_z_vel",-1),
   
   (set_fixed_point_multiplier, 100),
   (copy_position,pos49,pos9), # pos49 is prop pos.
   (call_script, "script_find_or_create_scene_prop_instance", ":ammo_size", 0, 0, 0),
   (assign,":ball_instance_id",reg0),

   (scene_prop_set_slot,":ball_instance_id", scene_prop_slot_in_use, 1),
   (scene_prop_set_slot,":ball_instance_id", scene_prop_slot_x_value, ":init_x_vel"),
   (scene_prop_set_slot,":ball_instance_id", scene_prop_slot_y_value, 0),
   (scene_prop_set_slot,":ball_instance_id", scene_prop_slot_z_value, ":init_z_vel"),
   (scene_prop_set_slot,":ball_instance_id", scene_prop_slot_time, 0),
   (scene_prop_set_slot,":ball_instance_id", scene_prop_slot_bounces, 0),
   (scene_prop_set_slot,":ball_instance_id", scene_prop_slot_user_agent, ":agent_id"),
   (scene_prop_set_slot,":ball_instance_id", scene_prop_slot_ammo_type, cannon_ammo_type_round),
   
   (call_script,"script_multiplayer_handle_prop_effect",":ball_instance_id",prop_effect_type_sound,":flight_sound_id",prop_effect_handle_start),
  ])]],


  # cannon dummy for canister
["cannon_ball_dummy", "{!}cannon_ball_dummy", [("Russian_gusarskiy_karabin",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|custom_kill_info(1),itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(150) | shoot_speed(200) | thrust_damage(300 ,pierce)|max_ammo(100)|accuracy(75),imodbits_none,
 []],
["cannon_canister_dummy", "{!}cannon_canister_dummy", [("Russian_gusarskiy_karabin",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|custom_kill_info(2),itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(150) | shoot_speed(200) | thrust_damage(300 ,pierce)|max_ammo(100)|accuracy(75),imodbits_none,
 []],
["cannon_explosion_dummy", "{!}cannon_ball_dummy", [("Russian_gusarskiy_karabin",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|custom_kill_info(3),itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(150) | shoot_speed(200) | thrust_damage(300 ,pierce)|max_ammo(100)|accuracy(75),imodbits_none,
 []],
["drown_dummy", "{!}cannon_ball_dummy", [("Russian_gusarskiy_karabin",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|custom_kill_info(4),itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(150) | shoot_speed(200) | thrust_damage(300 ,pierce)|max_ammo(100)|accuracy(75),imodbits_none,
 []],
["admin_kill_dummy", "{!}cannon_ball_dummy", [("Russian_gusarskiy_karabin",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|custom_kill_info(5),itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(150) | shoot_speed(200) | thrust_damage(300 ,pierce)|max_ammo(100)|accuracy(75),imodbits_none,
 []],


 
#Muskets
# French
["french_charleville", "Infantry Musket", [("french_charleville",0)], itp_cant_use_on_horseback|itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.5)|difficulty(0)|spd_rtng(23) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(75),imodbits_none,[]],
# [(ti_on_weapon_attack, [(store_trigger_param_1,":user_agent"),(call_script, "script_server_fire_musket", ":user_agent", firearm_type_musket),])]],
["french_charleville_melee", "Infantry Musket", [("french_charleville",0)], itp_cant_use_on_horseback|itp_has_upper_stab|itp_type_polearm |itp_primary|itp_is_pike|itp_no_blur,itc_spear|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(138)|swing_damage(40 ,  pierce) | thrust_damage(45 ,  pierce),imodbits_none ],
["french_versailles", "Infantry Musket", [("french_versailles",0)], itp_cant_use_on_horseback|itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.5)|difficulty(0)|spd_rtng(23) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(75),imodbits_none,[]],
# [(ti_on_weapon_attack, [(store_trigger_param_1,":user_agent"),(call_script, "script_server_fire_musket", ":user_agent", firearm_type_musket),])]],
["french_versailles_melee", "Infantry Musket", [("french_versailles",0)], itp_cant_use_on_horseback|itp_has_upper_stab|itp_type_polearm |itp_primary|itp_is_pike|itp_no_blur,itc_spear|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(138)|swing_damage(40 ,  pierce) | thrust_damage(45 ,  pierce),imodbits_none ], #patch1115 fix 28/4

["throwing_spears2",         "Throwing Spears", [("jarid_new_b",0),("jarid_new_b_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
525 , weight(3)|difficulty(0)|spd_rtng(87) | shoot_speed(22) | thrust_damage(44 ,  pierce)|max_ammo(4)|weapon_length(65),imodbits_thrown ],
["throwing_spear2_melee",         "Throwing Spear", [("jarid_new_b",0),("javelins_quiver", ixmesh_carry)],itp_type_polearm|itp_primary|itp_wooden_parry , itc_spear, 
525 , weight(1)|difficulty(0)|spd_rtng(91) | swing_damage(18, cut) | thrust_damage(23 ,  pierce)|weapon_length(75),imodbits_thrown ],

["arrow_b",         "Throwing Spears", [("arrow_b",0),("quiver_b", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
525 , weight(1)|difficulty(0)|spd_rtng(87) | shoot_speed(22) | thrust_damage(80 ,  pierce)|max_ammo(6)|weapon_length(75),imodbits_thrown ],
["arrow_b_melee",         "Throwing Spear", [("arrow_b",0),("quiver_b", ixmesh_carry)],itp_type_polearm|itp_primary|itp_wooden_parry , itc_spear, 
525 , weight(1)|difficulty(0)|spd_rtng(91) | swing_damage(20, cut) | thrust_damage(120 ,  pierce)|weapon_length(75),imodbits_thrown ],

["gekokujo_shuriken", "Shuriken", [("gekokujo_shuriken", 0), ("gekokujo_shuriken", ixmesh_flying_ammo)], itp_type_thrown|itp_merchandise|itp_primary|itp_secondary, itcf_throw_stone, 
93, weight(2)|difficulty(0)|spd_rtng(110)|shoot_speed(24)|abundance(100)|thrust_damage(35, cut)|max_ammo(6), imodbits_thrown, [] ],

["throwing_daggers", "Throwing Daggers", [("throwing_dagger",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_stone, 
193 , weight(2.5)|difficulty(0)|spd_rtng(110) | shoot_speed(24) | thrust_damage(25 ,  cut)|max_ammo(13)|weapon_length(0),imodbits_thrown ],

["throwing_spears3",         "Heavy Throwing Spears", [("touqiang",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin, 
525 , weight(3)|difficulty(0)|spd_rtng(87) | shoot_speed(22) | thrust_damage(60 ,  pierce)|max_ammo(1)|weapon_length(65),imodbits_thrown ],
["throwing_spear3_melee",    "Heavy Throwing Spear", [("touqiang",0)],itp_type_polearm|itp_primary|itp_wooden_parry , itc_spear, 
525 , weight(1)|difficulty(0)|spd_rtng(89) | swing_damage(18, cut) | thrust_damage(23 ,  pierce)|weapon_length(125),imodbits_thrown ],

["heavy_throwing_axes", "Heavy Throwing Axes", [("throwing_axe_b",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee,itcf_throw_axe,
620, weight(5)|difficulty(0)|spd_rtng(97) | shoot_speed(18) | thrust_damage(44,cut)|max_ammo(4)|weapon_length(53),imodbits_thrown_minus_heavy ],
["heavy_throwing_axes_melee", "Heavy Throwing Axe", [("throwing_axe_b",0)], itp_type_one_handed_wpn |itp_primary|itp_bonus_against_shield,itc_scimitar,
620, weight(1)|difficulty(0)|spd_rtng(97) | swing_damage(32,cut)|weapon_length(53),imodbits_thrown_minus_heavy ],

["stones",         "Stones", [("throwing_stone",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_stone, 
1 , weight(4)|difficulty(0)|spd_rtng(97) | shoot_speed(20) | thrust_damage(11 ,  blunt)|max_ammo(18)|weapon_length(8),imodbit_large_bag ],
#Ming Twohand weapon
["greatming_pudao", "GreatMing Pudao", [("cjpudao",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_bow_back|itc_guandao2,
 180 , weight(3.0)|difficulty(0)|spd_rtng(80) | weapon_length(180)|swing_damage(45 ,  cut) | thrust_damage(40 ,  pierce),imodbits_polearm ],
 
["greatming_short_pudao", "GreatMing short Pudao", [("pudao",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_bow_back|itc_guandao2,
 180 , weight(3.0)|difficulty(0)|spd_rtng(90) | weapon_length(137)|swing_damage(55 ,  cut) | thrust_damage(45 ,  pierce),imodbits_polearm ],

["greatming_axe", "GreatMing great axe", [("ch_b",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry, itcf_carry_bow_back|itc_guandao2,
 180 , weight(3.0)|difficulty(0)|spd_rtng(85) | weapon_length(133)|swing_damage(65 ,  cut) | thrust_damage(25 ,  blunt),imodbits_polearm ],
 
["goulian", "GreatMing voulge spear", [("guisarme_a",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur,  itcf_carry_spear|itc_guandao2,
 180 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(200)|swing_damage(45 ,  cut) | thrust_damage(40 ,  pierce),imodbits_polearm ],
 
["langxian", "Bamboo Toxic spear", [("Langxian",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 180 , weight(3.0)|difficulty(0)|spd_rtng(80) | weapon_length(330)|swing_damage(34 ,  cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],
 
["ming_spear4",  "Ming war spear", [("Txz_hyq",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry|itp_is_pike|itp_no_blur, itc_lance|itcf_carry_spear,
  80 , weight(2.25)|difficulty(0)|spd_rtng(98) | weapon_length(200)|swing_damage(26 , blunt) | thrust_damage(36 ,  pierce),imodbits_polearm ],

["sanjiaoha", "Ming Fork", [("DaMing_sanjiaocha",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry|itp_is_pike|itp_no_blur, itc_lance|itcf_carry_spear,
  80 , weight(3.5)|difficulty(0)|spd_rtng(90) | weapon_length(220)|swing_damage(20 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],

["qing_dadao", "Dadao", [("dadao",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_guandao2,
 180 , weight(3.0)|difficulty(0)|spd_rtng(85) | weapon_length(165)|swing_damage(50 ,  cut) | thrust_damage(40 ,  pierce),imodbits_polearm ],

["qing_spear", "Lance", [("qiang",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itc_lance,
 180 , weight(2.5)|difficulty(0)|spd_rtng(76) | weapon_length(200)|swing_damage(25 ,  pierce) | thrust_damage(30 ,  pierce),imodbits_polearm ],
 
["yumi_spear_melee",  "Yumi with spear", [("mtgong_lazhi",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry|itp_is_pike|itp_no_blur, itc_lance|itcf_carry_spear,
  80 , weight(2.25)|difficulty(0)|spd_rtng(98) | weapon_length(150)|swing_damage(26 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],
 
["horse_mandible_pike", "Mandible pike", [("horse_mandible_pike",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_guandao2,
 180 , weight(3.0)|difficulty(0)|spd_rtng(80) | weapon_length(165)|swing_damage(48 ,  blunt) | thrust_damage(20 ,  blunt),imodbits_polearm ],
 
["horse_mandible_pike2", "Mandible pike", [("horse_mandible_pike_d",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_guandao2,
 180 , weight(3.0)|difficulty(0)|spd_rtng(85) | weapon_length(165)|swing_damage(48 ,  blunt) | thrust_damage(20 ,  blunt),imodbits_polearm ],
 
#Cav sword
 ["sword_renai", "Renai Sword", [("side_sword",0),("side_sword_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 650 , weight(1.25)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(30 , cut) | thrust_damage(31 ,  pierce),imodbits_sword_high],


#Pike

["5m_greatpike","5M Pike", [("pike_500mm_cut",0)], itp_has_upper_stab|itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_no_parry|itp_two_handed|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 125 , weight(3.0)|difficulty(0)|spd_rtng(70) | weapon_length(500)|swing_damage(0 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],
 
["spanish_phalanx_pike","Spanish phalanx pike", [("asd4",0)], itp_has_upper_stab|itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_no_parry|itp_two_handed|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 125 , weight(4.0)|difficulty(0)|spd_rtng(70) | weapon_length(650)|swing_damage(0 , blunt) | thrust_damage(35 ,  pierce),imodbits_polearm ],
 
["yari1","Yari(Black)", [("sjqiang",0)], itp_has_upper_stab|itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_no_parry|itp_two_handed|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance2,
 125 , weight(2.0)|difficulty(0)|spd_rtng(80) | weapon_length(355)|swing_damage(20 , blunt) | thrust_damage(37 ,  pierce),imodbits_polearm ],
 
["yari2","Yari", [("ssqiang",0)], itp_has_upper_stab|itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_no_parry|itp_two_handed|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance2,
 125 , weight(2.0)|difficulty(0)|spd_rtng(80) | weapon_length(355)|swing_damage(22 , blunt) | thrust_damage(40 ,  pierce),imodbits_polearm ],
 
["euphorbia_pulcherrima","Euphorbia pulcherrima", [("alebarda",0)], itp_has_upper_stab|itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_no_parry|itp_two_handed|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_guandao2,
 125 , weight(2.0)|difficulty(0)|spd_rtng(80) | weapon_length(160)|swing_damage(40 , cut) | thrust_damage(35 ,  pierce),imodbits_polearm ],
 
 
["16tqiang01","Inca spear", [("16tqiang01",0)], itp_has_upper_stab|itp_type_polearm|itp_merchandise|itp_primary|itp_penalty_with_shield|itp_no_parry|itp_two_handed|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance2,
 125 , weight(1.8)|difficulty(0)|spd_rtng(80) | weapon_length(213)|swing_damage(20 , blunt) | thrust_damage(37 ,  pierce),imodbits_polearm ],
 
["osman_spear","Ottman spear", [("spear_h_2-15m",0)], itp_type_polearm|itp_primary|itp_wooden_parry , itc_spear|itcf_carry_spear, 
 125 , weight(1.8)|difficulty(0)|spd_rtng(80) | weapon_length(160)|swing_damage(38 , blunt) | thrust_damage(40 ,  pierce),imodbits_polearm ],
 
["osman_lance","Ottoman Lance", [("sipahlance3",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 125 , weight(2.5)|difficulty(0)|spd_rtng(80) | weapon_length(225)|swing_damage(20 , blunt) | thrust_damage(37 ,  pierce),imodbits_polearm ],
 
["osman_lance_broken","Ottoman Lance", [("sipahlance3_broken",0)], itp_has_upper_stab|itp_type_polearm| itp_primary|itp_two_handed|itp_wooden_parry, itcf_carry_spear|itc_spear,
 125 , weight(1.5)|difficulty(0)|spd_rtng(85) | weapon_length(110)|swing_damage(20 , blunt) | thrust_damage(15 ,  blunt),imodbits_polearm ],
 
["mamluk_carbine","Mamluk carbine", [("arabian_spear_a_3m",0)], itp_has_upper_stab|itp_type_polearm|itp_merchandise|itp_primary|itp_penalty_with_shield|itp_no_parry|itp_two_handed|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 125 , weight(1.8)|difficulty(0)|spd_rtng(80) | weapon_length(200)|swing_damage(30 , blunt) | thrust_damage(45 ,  pierce),imodbits_polearm ],
 
["cavalry_spear2","Cavalry spear", [("spear_f_2_9m",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance2,
 125 , weight(1.5)|difficulty(0)|spd_rtng(80) | weapon_length(175)|swing_damage(20 , blunt) | thrust_damage(37 ,  pierce),imodbits_polearm ],
 
["russian_militia_spear","Russian militia spear", [("spear_i_2-3m",0)],itp_type_polearm|itp_primary|itp_wooden_parry|itc_spear ,itc_lance,
 125 , weight(3.0)|difficulty(0)|spd_rtng(90) | weapon_length(105)|swing_damage(0 , blunt) | thrust_damage(32 ,  pierce),imodbits_polearm ],
 
 
["honda_spear", "Honda war spear", [("pljq",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_guandao2,
 180 , weight(3.5)|difficulty(0)|spd_rtng(88) | weapon_length(200)|swing_damage(55 ,  cut) | thrust_damage(45 ,  pierce),imodbits_polearm ],
 
# British
["british_brown_bess", "Infantry Musket", [("brown_bess_musket",0)], itp_cant_use_on_horseback|itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.5)|difficulty(0)|spd_rtng(23) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(75),imodbits_none,[]],
["british_brown_bess_melee", "Infantry Musket", [("brown_bess_musket",0)], itp_cant_use_on_horseback|itp_has_upper_stab|itp_type_polearm |itp_primary|itp_is_pike|itp_no_blur,itc_spear|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(138)|swing_damage(40 ,  pierce) | thrust_damage(45 ,  pierce),imodbits_none ], 

 #Ming blunderbuss
["ming_sanyanchong", "Ming Sanyanchong", [("DaMing_sanyanchong",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_throw_knife|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(12) | shoot_speed(150) | thrust_damage(80 ,pierce)|max_ammo(3)|accuracy(50),imodbits_none,[]],

["ming_sanyanchong__melee", "Ming Sanyanchong", [("DaMing_sanyanchong",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 660 , weight(3.0)|difficulty(0)|spd_rtng(85) | weapon_length(100)|swing_damage(30 , blunt) | thrust_damage(0 ,  pierce),imodbits_axe ],

["ming_sanyanchong_q", "Ming Sanyanchong(Muity-fire mode)", [("DaMing_sanyanchong",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_throw_knife|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(12) | shoot_speed(150) | thrust_damage(80 ,pierce)|max_ammo(3)|accuracy(50),imodbits_none, 
[(ti_on_weapon_attack, [
  (this_or_next|multiplayer_is_server),
  (neg|game_in_multiplayer_mode),
  (store_trigger_param_1,":agent_id"),
  (agent_set_slot,":agent_id", slot_sanyanchong_fire,1),
  ])]],

["ming_sanyanchong_q_melee", "Ming Sanyanchong(Muity-fire mode)", [("DaMing_sanyanchong",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 660 , weight(3.0)|difficulty(0)|spd_rtng(85) | weapon_length(100)|swing_damage(30 , blunt) | thrust_damage(0 ,  pierce),imodbits_axe ],

["ming_blunderbuss", "Ming blunderbuss", [("Danyanhuochong",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_throw_knife|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(15) | shoot_speed(150) | thrust_damage(80 ,pierce)|max_ammo(1)|accuracy(30),imodbits_none,
 [(ti_on_weapon_attack, [
  (this_or_next|multiplayer_is_server),
  (neg|game_in_multiplayer_mode),
  (store_trigger_param_1,":agent_id"),
  (eq,":agent_id",":agent_id"), # fix compiler bug warning.
  (copy_position,pos22,pos1),
  (position_move_y,pos22,110),
  (try_for_range,":unused",0,6), #4 extra bullets + 1 original = 5 bullets in one shot :D
    (copy_position,pos23,pos22),
    (store_random_in_range,":x_change",-15,16),
    (store_random_in_range,":z_change",-15,16),
    (position_rotate_x, pos23, ":x_change"),
    (position_rotate_z, pos23, ":z_change"),
    (set_fixed_point_multiplier,100),
    (store_random_in_range,":bullet_speed",12000,16000),
    (add_missile, ":agent_id", pos23, ":bullet_speed", "itm_cannon_canister_dummy", 0, "itm_canister_ammo", 0),
  (try_end),
  ])]],

["ming_blunderbuss__melee", "Ming Sanyanchong", [("Danyanhuochong",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_unbalanced, itc_nodachi|itcf_carry_axe_back,
 660 , weight(3.0)|difficulty(0)|spd_rtng(85) | weapon_length(100)|swing_damage(30 , blunt) | thrust_damage(0 ,  pierce),imodbits_axe ],
 
["ming_rocketluncher", "Ming rocketluncher", [("BaiHuQiBen",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_while_moving_mounted|itp_cant_reload_while_moving ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(5.0)|difficulty(0)|spd_rtng(10) | shoot_speed(40) | thrust_damage(80 ,pierce)|max_ammo(1)|accuracy(35),imodbits_none, 
 [(ti_on_weapon_attack, [
  (this_or_next|multiplayer_is_server),
  (neg|game_in_multiplayer_mode),
  (store_trigger_param_1,":agent_id"),
  (eq,":agent_id",":agent_id"), # fix compiler bug warning.
  (copy_position,pos22,pos1),
  (position_move_y,pos22,110),
  (try_for_range,":unused",0,20), #20 extra bullets + 1 original = 21 bullets in one shot XD
    (copy_position,pos23,pos22),
    (store_random_in_range,":x_change",-14,15),
    (store_random_in_range,":z_change",-14,15),
    (position_rotate_x, pos23, ":x_change"),
    (position_rotate_z, pos23, ":z_change"),
    (set_fixed_point_multiplier,100),
    (store_random_in_range,":bullet_speed",8000,16000),
    (add_missile, ":agent_id", pos23, ":bullet_speed", "itm_rocketarrows_dummy", 20, "itm_rocketarrows", 10),
  (try_end),
  ])]],
 

["cavalry_pika_a", "Cavalry Lance", [("cavalry_lance_a",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance2,
 500 , weight(1.1)|difficulty(6)|spd_rtng(88) | weapon_length(160)|swing_damage(0 , cut) | thrust_damage(22 ,  pierce),imodbits_polearm ],
 
["cavalry_lance_b", "Cavalry Lance", [("spear_f_2-9m",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 500 , weight(1.1)|difficulty(6)|spd_rtng(88) | weapon_length(190)|swing_damage(0 , cut) | thrust_damage(35 ,  pierce),imodbits_polearm ],

["cavalry_lance_b_break", "Broken lance", [("qiqiangzhedua",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance2,
 500 , weight(0.5)|difficulty(6)|spd_rtng(88) | weapon_length(95)|swing_damage(0 , cut) | thrust_damage(10 ,  blunt),imodbits_polearm ],
# Russian
["russian_musket_1808", "Infantry Musket", [("Russian_musket_1808",0)], itp_cant_use_on_horseback|itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.5)|difficulty(0)|spd_rtng(23) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(75),imodbits_none,[]],
# [(ti_on_weapon_attack, [(store_trigger_param_1,":user_agent"),(call_script, "script_server_fire_musket", ":user_agent", firearm_type_musket),])]],
["russian_musket_1808_melee", "Infantry Musket", [("Russian_musket_1808",0)], itp_cant_use_on_horseback|itp_has_upper_stab|itp_type_polearm |itp_primary|itp_is_pike|itp_no_blur,itc_spear|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(138)|swing_damage(40 ,  pierce) | thrust_damage(45 ,  pierce),imodbits_none ], #patch1115 fix 28/3

["ming_shieldofficer", "Ming Shield", [("DaMing_tengpai",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
 42 , weight(4.0)|shield_width(36)|hit_points(330)|body_armor(16)|spd_rtng(90),imodbits_shield ],

# Austrian
["austrian_musket", "Infantry Musket", [("austrian_musket",0)], itp_cant_use_on_horseback|itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.5)|difficulty(0)|spd_rtng(23) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(75),imodbits_none,[]],
["austrian_musket_melee", "Infantry Musket", [("austrian_musket",0)], itp_cant_use_on_horseback|itp_has_upper_stab|itp_type_polearm |itp_primary|itp_is_pike|itp_no_blur,itc_spear|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(138)|swing_damage(40 ,  pierce) | thrust_damage(45 ,  pierce),imodbits_none ], #patch1115 fix 28/2

# Prussian
["prussian_potsdam", "Infantry Musket", [("potsdam_musket",0)], itp_cant_use_on_horseback|itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.5)|difficulty(0)|spd_rtng(23) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(75),imodbits_none,[]],
["prussian_potsdam_melee", "Infantry Musket", [("potsdam_musket",0)], itp_cant_use_on_horseback|itp_has_upper_stab|itp_type_polearm |itp_primary|itp_is_pike|itp_no_blur,itc_spear|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(138)|swing_damage(40 ,  pierce) | thrust_damage(45 ,  pierce),imodbits_none ], #patch1115 fix 28/1

# Rhine
["prussian_musket_1806", "Infantry Musket", [("prussian_kuhfuss",0)], itp_cant_use_on_horseback|itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.5)|difficulty(0)|spd_rtng(23) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(75),imodbits_none,[]],
["prussian_musket_1806_melee", "Infantry Musket", [("prussian_kuhfuss",0)], itp_cant_use_on_horseback|itp_has_upper_stab|itp_type_polearm |itp_primary|itp_is_pike|itp_no_blur,itc_spear|itcf_carry_crossbow_back,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(138)|swing_damage(40 ,  pierce) | thrust_damage(45 ,  pierce),imodbits_none ], 
# boland
["bolanqibingshouqiang1", "bolanqibingshouqiang1", [("pistol_2stwol",0)], itp_cant_use_on_horseback|itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.5)|difficulty(0)|spd_rtng(23) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(75),imodbits_none,[]],
["bolanqibingshouqiang2", "bolanqibingshouqiang2", [("pistol_2stwolB",0)], itp_cant_use_on_horseback|itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|itp_cant_reload_on_horseback|itp_cant_reload_while_moving|itp_next_item_as_melee ,itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.5)|difficulty(0)|spd_rtng(23) | shoot_speed(250) | thrust_damage(100 ,pierce)|max_ammo(1)|accuracy(75),imodbits_none,[]],
#刀剑
 # Swords
# French
 ["french_art_off_sword","Artillery Officer Sword", [("Artillery_officer_sword",0),("Artillery_officer_sword_in_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.5)|difficulty(0)|spd_rtng(92) | weapon_length(108)|swing_damage(32 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ],
 ["ming_saber","Ming Saber", [("DaMing_yaodao",0),("DaMing_yaodao_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.5)|difficulty(0)|spd_rtng(92) | weapon_length(96)|swing_damage(32 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ],
 ["ming_miao_saber","Ming miao saber", [("Zhonghua_miaodao",0),("Zhonghua_miaodao_qiao",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
210 , weight(1.5)|difficulty(0)|spd_rtng(85) | weapon_length(100)|swing_damage(50, cut) | thrust_damage(35,  pierce),imodbits_sword_high ],
 ["french_carabineer_sword","Ming Guduo", [("DaMing_guduo",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_unbalanced, itc_morningstar|itcf_carry_mace_left_hip, 
210 , weight(2.0)|difficulty(0)|spd_rtng(90) | weapon_length(115)|swing_damage(36 , blunt) | thrust_damage(32 ,  blunt),imodbits_sword_high ], #Ming blunt
 ["qijiadao","Qi Army Saber", [("QiJiaDao",0),("QiJiaDao_qiao",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_next_item_as_melee, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.5)|difficulty(0)|spd_rtng(94) | weapon_length(95)|swing_damage(36, cut) | thrust_damage(32,  pierce),imodbits_sword_high ],
 ["qijiadao2","Qi Army Saber", [("QiJiaDao",0),("QiJiaDao_qiao",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
210 , weight(1.5)|difficulty(0)|spd_rtng(94) | weapon_length(95)|swing_damage(44, cut) | thrust_damage(37,  pierce),imodbits_sword_high ],
 ["xiuchundao","Imperial Guard Saber", [("XiuChunDao",0),("XiuChunDao_qiao",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(95)|swing_damage(40, cut) | thrust_damage(35,  pierce),imodbits_sword_high ],
 ["qing_saber","Qing Saber", [("qing_niuwei",0),("qing_niuwei_s",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.5)|difficulty(0)|spd_rtng(92) | weapon_length(90)|swing_damage(35 , cut) | thrust_damage(32 ,  pierce),imodbits_sword_high ],
 ["french_briquet_garde","Guard Sabre Briquet", [("Garde_briquet",0),("Guard_briquet_in_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(95) | weapon_length(77)|swing_damage(22 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
 ["french_light_cav_sabre_garde","Light Cavalry Sabre", [("Garde_light_cav_sabre",0),("Garde_light_cav_sabre_in_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(2.0)|difficulty(0)|spd_rtng(93) | weapon_length(102)|swing_damage(33 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ], #patch1115 fix 44/9
 ["french_heavy_cav_sabre_garde","Heavy Cavalry Sabre", [("Guard_heavy_cavalry_sabre",0),("Guard_heavy_cavalry_sabre_in_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(3.0)|difficulty(0)|spd_rtng(91) | weapon_length(111)|swing_damage(36 , cut) | thrust_damage(32 ,  pierce),imodbits_sword_high ], #patch1115 fix 44/8
 ["french_inf_off_sabre_garde","Imperial Guard Officer Sabre", [("Guard_infantry_officer_sabre",0),("Guard_infantry_officer_sabre_in_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.5)|difficulty(0)|spd_rtng(95) | weapon_length(97)|swing_damage(32 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ],
 ["french_heavy_cav_off_sabre","Heavy Cavalry Sabre", [("Officer_heavy_cavalry_sword",0),("Officer_heavy_cavalry_sword_in_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(3.0)|difficulty(0)|spd_rtng(91) | weapon_length(111)|swing_damage(36 , cut) | thrust_damage(32 ,  pierce),imodbits_sword_high ], #patch1115 fix 44/5
 ["french_inf_off_sabre","Infantry Sabre", [("Infantry_officer_sword",0),("Infantry_officer_sword_in_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.5)|difficulty(0)|spd_rtng(95) | weapon_length(100)|swing_damage(32 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ],
 ["french_light_cav_off_sabre","Light Cavalry Sabre", [("Officer_light_cav_sabre",0),("Officer_light_cav_sabre_in_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(2.0)|difficulty(0)|spd_rtng(93) | weapon_length(102)|swing_damage(33 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ], #patch1115 fix 44/6
 ["french_light_inf_off_sabre","Light Infantry Sabre", [("Saber_voltigeur",0),("Saber_voltigeur_in_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.5)|difficulty(0)|spd_rtng(95) | weapon_length(97)|swing_damage(32 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ],
 ["french_line_cav_sabre","Line Cavalry Sabre", [("Line_cav_ANXIII",0),("Line_cav_ANXIII_in_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
210 , weight(3.0)|difficulty(0)|spd_rtng(91) | weapon_length(111)|swing_damage(36 , cut) | thrust_damage(32 ,  pierce),imodbits_sword_high ], #patch1115 fix 44/7
 ["french_briquet","Sabre Briquet", [("Sabre_briquet_french",0),("sabre_briquetscab",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(95) | weapon_length(63)|swing_damage(22 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
 ["french_light_cav_sabre","Light Cavalry Sabre", [("Sabre_cavalerie_legere",0),("Sabre_cavalerie_legere_in_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(2.0)|difficulty(0)|spd_rtng(93) | weapon_length(102)|swing_damage(33 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ],
 ["french_sappeur_sword","Sapper Sword", [("Sappeur_sword",0),("Sappeur_sword_in_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(95) | weapon_length(72)|swing_damage(22 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ], 

["katana_1","Katana", [("ggekokujo_katana_1", 0), ("ggekokujo_katana_1_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_katana|itcf_show_holster_when_drawn, 
210 , weight(2)|difficulty(0)|spd_rtng(105) | weapon_length(78)|swing_damage(40 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],

["katana_2","Katana", [("ggekokujo_tachi_2", 0), ("ggekokujo_tachi_2_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_katana|itcf_show_holster_when_drawn, 
210 , weight(2)|difficulty(0)|spd_rtng(105) | weapon_length(89)|swing_damage(40 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],

["tachi_7","Tachi", [("ggekokujo_tachi_7", 0), ("ggekokujo_tachi_7_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_katana|itcf_show_holster_when_drawn, 
210 , weight(2)|difficulty(0)|spd_rtng(105) | weapon_length(89)|swing_damage(40 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],

["tachi_5","Tachi", [("ggekokujo_tachi_5", 0), ("ggekokujo_tachi_5_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_katana|itcf_show_holster_when_drawn, 
210 , weight(2)|difficulty(0)|spd_rtng(105) | weapon_length(89)|swing_damage(40 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],

["katana_3","Katana", [("ggekokujo_katana_3", 0), ("ggekokujo_katana_3_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_katana|itcf_show_holster_when_drawn, 
210 , weight(2)|difficulty(0)|spd_rtng(103) | weapon_length(78)|swing_damage(40 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],

["tachi_1","Tachi", [("ggekokujo_tachi_1", 0), ("ggekokujo_tachi_1_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_katana|itcf_show_holster_when_drawn, 
210 , weight(2)|difficulty(0)|spd_rtng(105) | weapon_length(89)|swing_damage(40 , cut) | thrust_damage(22 ,  pierce),imodbits_sword_high ],


["spanish_sword","Spanish Sword", [("spain_rapier_a",0),("spain_rapier_a_scab",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.5)|difficulty(0)|spd_rtng(95) | weapon_length(105)|swing_damage(20, cut) | thrust_damage(45,  pierce),imodbits_sword_high ],

["rapier","Rapier Sword", [("rapier_a",0),("rapier_a_scab",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.5)|difficulty(0)|spd_rtng(100) | weapon_length(100)|swing_damage(25, cut) | thrust_damage(30,  pierce),imodbits_sword_high ],

["short_sword","Short Sword", [("inf_dussack_a",0),("inf_dussack_a_scab",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(100) | weapon_length(72)|swing_damage(22 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],

["qing_war_sword","Qing war sword", [("qing_changdao",0),("qing_changdao_s",ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_merchandise| itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn,
210 , weight(1.5)|difficulty(0)|spd_rtng(85) | weapon_length(100)|swing_damage(50, cut) | thrust_damage(35,  pierce),imodbits_sword_high ],

["wakizashi_3", "Wakizashi", [("ggekokujo_wakizashi_3", 0), ("ggekokujo_wakizashi_3_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary, itcf_thrust_onehanded|itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_parry_forward_onehanded|itcf_parry_up_onehanded|itcf_parry_right_onehanded|itcf_parry_left_onehanded|itcf_show_holster_when_drawn|itcf_carry_wakizashi, 
321, weight(1.25)|weapon_length(59)|difficulty(0)|spd_rtng(115)|abundance(105)|swing_damage(25, cut)|thrust_damage(19, pierce), imodbits_sword_high, [] ],

["wakizashi_1", "Wakizashi", [("ggekokujo_wakizashi_1", 0), ("ggekokujo_wakizashi_1_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary, itcf_thrust_onehanded|itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_parry_forward_onehanded|itcf_parry_up_onehanded|itcf_parry_right_onehanded|itcf_parry_left_onehanded|itcf_show_holster_when_drawn|itcf_carry_wakizashi, 
321, weight(1.25)|weapon_length(59)|difficulty(0)|spd_rtng(115)|abundance(105)|swing_damage(25, cut)|thrust_damage(19, pierce), imodbits_sword_high, [] ],

["wakizashi_7", "Wakizashi", [("ggekokujo_wakizashi_7", 0), ("ggekokujo_wakizashi_7_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary, itcf_thrust_onehanded|itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_parry_forward_onehanded|itcf_parry_up_onehanded|itcf_parry_right_onehanded|itcf_parry_left_onehanded|itcf_show_holster_when_drawn|itcf_carry_wakizashi, 
321, weight(1.25)|weapon_length(59)|difficulty(0)|spd_rtng(115)|abundance(105)|swing_damage(25, cut)|thrust_damage(19, pierce), imodbits_sword_high, [] ],

["ninjato_1", "Ninjato", [("gekokujo_ninjato_1", 0), ("gekokujo_ninjato_1_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_thrust_onehanded|itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_parry_forward_onehanded|itcf_parry_up_onehanded|itcf_parry_right_onehanded|itcf_parry_left_onehanded|itcf_show_holster_when_drawn|itcf_carry_sword_back, 
432, weight(1.5)|weapon_length(50)|difficulty(0)|spd_rtng(120)|abundance(90)|swing_damage(33, cut)|thrust_damage(30, pierce), imodbits_sword_high, [] ],

["ninjato_4", "Ninjato", [("gekokujo_ninjato_4", 0), ("gekokujo_ninjato_4_scabbard", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itcf_thrust_onehanded|itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded|itcf_thrust_twohanded|itcf_overswing_twohanded|itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_parry_forward_twohanded|itcf_parry_up_twohanded|itcf_parry_right_twohanded|itcf_parry_left_twohanded|itcf_show_holster_when_drawn|itcf_carry_sword_back, 
512, weight(2.25)|weapon_length(69)|difficulty(0)|spd_rtng(110)|abundance(90)|swing_damage(35, cut)|thrust_damage(30, pierce), imodbits_sword_high, [] ],

["sahlander_cavalry_sword", "Sahlander cavalry sword", [("arabian_sword_c", 0), ("scab_arabian_sword_c.1", ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_primary, itcf_thrust_onehanded|itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded|itcf_thrust_twohanded|itcf_overswing_twohanded|itcf_slashright_twohanded|itcf_slashleft_twohanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_parry_forward_twohanded|itcf_parry_up_twohanded|itcf_parry_right_twohanded|itcf_parry_left_twohanded|itcf_show_holster_when_drawn|itcf_carry_sword_left_hip, 
512, weight(1.8)|weapon_length(101)|difficulty(0)|spd_rtng(110)|abundance(90)|swing_damage(45, cut)|thrust_damage(30, pierce), imodbits_sword_high, [] ],

["chekan_good", "Good Chekan", [("chekan_rich_a",0)], itp_type_one_handed_wpn|itp_merchandise|itp_secondary|itp_primary|itp_extra_penetration, itc_scimitar|itcf_carry_axe_left_hip,
 900 , weight(1.7)|difficulty(12)|spd_rtng(94) | weapon_length(70)|swing_damage(38 , pierce) | thrust_damage(0 ,  pierce),imodbits_pick ],

["palash", "Cavalry Broadsword", [("kava_palash_pure_a",0),("kava_palash_scabbard_a", ixmesh_carry)], itp_type_one_handed_wpn|itp_secondary|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
 200 , weight(1.7)|difficulty(9)|spd_rtng(84) | weapon_length(110)|swing_damage(35 , cut) | thrust_damage(30 ,  pierce),imodbits_sword ] ,

 ["ming_sword","Ming Sword", [("txz_weapon_a04_02j",0),("txz_weapon_a04_02q",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.7)|difficulty(0)|spd_rtng(90) | weapon_length(105)|swing_damage(36 , cut) | thrust_damage(36 ,  pierce),imodbits_sword_high ],

 ["ming_sword2","Ming Sword", [("cy_tiejian",0),("cy_tiejianp",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.5)|difficulty(0)|spd_rtng(93) | weapon_length(95)|swing_damage(30 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ],

["russian_chopper3","Russian saber", [("polyak_sablya_b",0),("polyak_sablya_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.2)|difficulty(0)|spd_rtng(92) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ],

 ["polish_axe_a", "Polich Axe 1", [("polish_axe_a",0)],#,("Axe_landwehr_scabbard",ixmesh_carry)],
 itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, #itcf_carry_sword_left_hip, #|itcf_show_holster_when_drawn,
 80,weight(0)|difficulty(9)|spd_rtng(90) | weapon_length(55)|swing_damage(33 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],#patch1115 56/1

 ["polish_axe_b", "Polich Axe 2", [("polish_axe_b",0)],#,("Axe_landwehr_scabbard",ixmesh_carry)],
 itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, #itcf_carry_sword_left_hip, #|itcf_show_holster_when_drawn,
 80,weight(0)|difficulty(9)|spd_rtng(90) | weapon_length(55)|swing_damage(33 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],#patch1115 56/1
 
 ["polish_axe_c", "Polich Axe 3", [("polish_axe_c",0)],#,("Axe_landwehr_scabbard",ixmesh_carry)],
 itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, #itcf_carry_sword_left_hip, #|itcf_show_holster_when_drawn,
 80,weight(0)|difficulty(9)|spd_rtng(90) | weapon_length(55)|swing_damage(33 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],#patch1115 56/1
 
["horse_mandible_pike", "Mandible pike 1", [("horse_mandible_pike",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_guandao2,
 180 , weight(3.0)|difficulty(0)|spd_rtng(80) | weapon_length(165)|swing_damage(48 ,  blunt) | thrust_damage(20 ,  blunt),imodbits_polearm ],
 
["horse_mandible_pike2", "Mandible pike 2", [("horse_mandible_pike_d",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_guandao2,
 180 , weight(3.0)|difficulty(0)|spd_rtng(85) | weapon_length(165)|swing_damage(48 ,  blunt) | thrust_damage(20 ,  blunt),imodbits_polearm ],
 
# Russian
 ["russian_sabre_1798","Light Cavalry Sabre", [("Russian_sabre_1798",0),("Russian_sabre_1798_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(2.0)|difficulty(0)|spd_rtng(93) | weapon_length(102)|swing_damage(33 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ], #patch1115 fix 44/11
 ["russian_sabre_1809","Light Cavalry Sabre", [("copy_qing_ppeidao",0),("copy_qing_ppeidao_s",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(2.0)|difficulty(0)|spd_rtng(93) | weapon_length(112)|swing_damage(33 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ], #patch1115 fix 44/10
 ["russian_sword_1810","Dragoon Sword", [("Russian_sword_1810",0),("Russian_sword_1810_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(2.0)|difficulty(0)|spd_rtng(91) | weapon_length(111)|swing_damage(33 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ], #patch1115 fix 44/3
 ["russian_guard_sword_1799","Heavy Cavalry Sword", [("Russian_guard_sword_1799",0),("Russian_guard_sword_1799_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(3.0)|difficulty(0)|spd_rtng(91) | weapon_length(111)|swing_damage(36 , cut) | thrust_damage(32 ,  pierce),imodbits_sword_high ], #patch1115 fix 44/1
 ["russian_briquet_1807","Sabre Briquet", [("Russian_briquet_1807",0),("Tesak_black_blackbelt_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(95) | weapon_length(63)|swing_damage(22 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
 ["russian_jaeger_bayonet","Sword Bayonet", [("Russian_jaeger_bayonet",0),("Kortik_in_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(95) | weapon_length(63)|swing_damage(22 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
 ["russian_jaeger_bayonet_jaeger","Sword Bayonet", [("Russian_jaeger_bayonet",0),("Kortik_in_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(95) | weapon_length(63)|swing_damage(22 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
 ["russian_officer_sword","Officer Sword", [("Russian_officer_sword",0),("Russian_officer_sword_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.5)|difficulty(0)|spd_rtng(95) | weapon_length(100)|swing_damage(32 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ],
 ["russian_officer_sword_jaeger","Officer Sword", [("Russian_officer_sword",0),("Russian_officer_sword_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.5)|difficulty(0)|spd_rtng(95) | weapon_length(100)|swing_damage(32 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ],
 ["russian_peasant_axe", "Hand Axe", [("Russian_peasant_axe",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, #itcf_carry_sword_left_hip,
87 , weight(1.5)|difficulty(9)|spd_rtng(90) | weapon_length(50)|swing_damage(33 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],#patch1115 56/2
 ["brokenbottle","Broken Vodka Bottle", [("Russian_vodka_bottle",0)], itp_type_thrown|itp_merchandise|itp_next_item_as_melee,itcf_throw_stone,
360, weight(1)|difficulty(0)|spd_rtng(90) | shoot_speed(16) | thrust_damage(33,cut)|max_ammo(1)|weapon_length(33),imodbits_none,
 [(ti_on_missile_hit, [(this_or_next|multiplayer_is_server),(neg|game_in_multiplayer_mode),(particle_system_burst, "psys_bottle_break", pos1, 10),(copy_position,pos56,pos1),(call_script,"script_multiplayer_server_play_sound_at_position","snd_glass_break"),])]],
 ["brokenbottle_melee", "Broken Vodka Bottle", [("Russian_vodka_bottle",0)], itp_type_one_handed_wpn|itp_primary|itp_no_parry, itc_dagger, 
210 , weight(1)|difficulty(0)|spd_rtng(95) | weapon_length(29)|swing_damage(22, blunt)| thrust_damage(20 ,  pierce),imodbits_sword_high ],
 ["russian_kindjal","Cossack Knife", [("Russian_kindjal",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left,
210 , weight(1)|difficulty(0)|spd_rtng(96) | weapon_length(45)|swing_damage(18 , cut) | thrust_damage(18 ,  pierce),imodbits_sword_high ],
 ["russian_guard_off_sword","Officer Sword", [("Russian_officer_sword",0),("Russian_officer_sword_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.5)|difficulty(0)|spd_rtng(95) | weapon_length(100)|swing_damage(33 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ],
 ["russian_sappeur_dagger","Short Sword", [("Russian_sappeur_dagger",0),("Sappeur_dagger_in_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(95) | weapon_length(64)|swing_damage(22 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
 ["russian_sappeur_dagger_invis","Short Sword", [("Russian_sappeur_dagger",0),("mm_invisible",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(95) | weapon_length(64)|swing_damage(22 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
 ["russian_peasant_knife","Knife", [("Russian_peasant_knife",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_left,
210 , weight(1)|difficulty(0)|spd_rtng(96) | weapon_length(27)|swing_damage(18 , cut) | thrust_damage(18 ,  pierce),imodbits_sword_high ],
 ["russian_peasant_serp","Sickle", [("Russian_peasant_serp",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger_no_stab|itcf_carry_dagger_front_left,
210 , weight(1)|difficulty(0)|spd_rtng(96) | weapon_length(35)|swing_damage(18 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
 ["mongo_saber","Mongo Saber", [("scimitar_b",0),("scab_scimeter_b",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(2.0)|difficulty(0)|spd_rtng(93) | weapon_length(102)|swing_damage(32 , cut) | thrust_damage(18 ,  pierce),imodbits_sword_high ], #patch1115 fix 44/11

["kama_1", "Kama", [("gekokujo_kama_1", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary, itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_parry_forward_onehanded|itcf_parry_up_onehanded|itcf_parry_right_onehanded|itcf_parry_left_onehanded|itcf_carry_axe_left_hip, 
9, weight(1)|weapon_length(67)|difficulty(0)|spd_rtng(100)|abundance(100)|swing_damage(22, cut)|thrust_damage(0, pierce), imodbits_axe, [] ],
["kama_2", "Kama", [("gekokujo_kama_2", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_wooden_parry|itp_primary, itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_parry_forward_onehanded|itcf_parry_up_onehanded|itcf_parry_right_onehanded|itcf_parry_left_onehanded|itcf_carry_axe_left_hip, 
220, weight(1)|weapon_length(72)|difficulty(0)|spd_rtng(100)|abundance(100)|swing_damage(26, pierce)|thrust_damage(0, pierce), imodbits_axe, [] ],

["kama_3", "Long Kama", [("nagigama", 0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_no_blur, itc_guandao2,
 125 , weight(2.7)|difficulty(0)|spd_rtng(75) | weapon_length(135)|swing_damage(36 , pierce) | thrust_damage(10, blunt),imodbits_polearm ],

["dou_knife","Dou knife", [("dou_knife",0),("dou_knife_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_parry_forward_onehanded|itcf_parry_up_onehanded|itcf_parry_right_onehanded|itcf_parry_left_onehanded|itcf_carry_dagger_front_right|itcf_show_holster_when_drawn, 
210 , weight(1.0)|difficulty(0)|spd_rtng(100) | weapon_length(55)|swing_damage(26 , cut) | thrust_damage(0 ,  pierce),imodbits_sword_high ], 

["sickle",         "Sickle", [("sickle",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver, 
9 , weight(1.5)|difficulty(0)|spd_rtng(99) | weapon_length(40)|swing_damage(20 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["cleaver",         "Cleaver", [("cleaver_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_wooden_parry, itc_cleaver, 
14 , weight(1.5)|difficulty(0)|spd_rtng(103) | weapon_length(35)|swing_damage(24 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["butchering_knife", "Butchering Knife", [("khyber_knife_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger|itcf_carry_dagger_front_right, 
23 , weight(0.75)|difficulty(0)|spd_rtng(108) | weapon_length(60)|swing_damage(24 , cut) | thrust_damage(17 ,  pierce),imodbits_sword ],

# British
 ["british_highlander_officer_sword","Highlander Officer Sword", [("scottish_broadsword",0),("scottish_broadsword_in_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(32 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ],
 ["british_heavy_cav_sword","Heavy Cavalry Sword", [("1796_heavy_cavalry_sword",0),("1796_heavy_cavalry_sword_in_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(3.0)|difficulty(0)|spd_rtng(91) | weapon_length(111)|swing_damage(36 , cut) | thrust_damage(32 ,  pierce),imodbits_sword_high ],
 ["british_light_cav_sabre","Light Cavalry Sabre", [("1796_light_cavalry_saber",0),("1796_light_cavalry_saber_in_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn,
210 , weight(2.0)|difficulty(0)|spd_rtng(93) | weapon_length(102)|swing_damage(33 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ], #patch1115 fix 44/2
 ["british_baker_bayonet","Sword Bayonet", [("British_baker_bayonet",0),("British_baker_bayonet_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(95) | weapon_length(63)|swing_damage(22 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
 ["british_musician_sword","Short Sword", [("British_musician_sword",0),("British_musician_sword_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(95) | weapon_length(63)|swing_damage(22 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
 ["british_musician_sword_invis","Short Sword", [("British_musician_sword",0),("mm_invisible",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(95) | weapon_length(63)|swing_damage(22 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
 ["british_officer_sword","Officer Sword", [("British_officer_sword",0),("British_officer_sword_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.5)|difficulty(0)|spd_rtng(95) | weapon_length(100)|swing_damage(32 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ],
 #v15 British_officer_sword replaces Russian one
 
#Austrian
#Austrian_infantry_briquet_scabbard
 ["austrian_infantry_briquet","Sword Bayonet", [("Austrian_infantry_briquet",0),("Austrian_infantry_briquet_black_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(95) | weapon_length(63)|swing_damage(22 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
 ["austrian_infantry_briquet_black","Sword Bayonet", [("Austrian_infantry_briquet",0),("Austrian_infantry_briquet_black_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(95) | weapon_length(63)|swing_damage(22 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
 ["austrian_jaeger_bayonet","Sword Bayonet", [("Austrian_jaeger_bayonet",0),("Austrian_jaeger_bayonet_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(95) | weapon_length(63)|swing_damage(22 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
 ["austrian_jaeger_bayonet_invis","Sword Bayonet", [("Austrian_jaeger_bayonet",0),("mm_invisible",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(95) | weapon_length(63)|swing_damage(22 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],


["german_bastard_sword",  "german bastard sword", [("twohand_sword_b",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 
 920 , weight(4.0)|difficulty(11)|spd_rtng(92) | weapon_length(85)|swing_damage(50 , cut) | thrust_damage(35 ,  pierce),imodbits_axe ],
 

["russian_militia_axe",  "Russian militia axe", [("lui_knightaxeonehe",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 
 920 , weight(2.0)|difficulty(11)|spd_rtng(92) | weapon_length(75)|swing_damage(35 , cut) | thrust_damage(28 ,  pierce),imodbits_axe ],
 
["badish_tomahawk",  "Badish tomahawk", [("berfish_oim_b",0)], itp_type_polearm|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 
 920 , weight(2.0)|difficulty(11)|spd_rtng(85) | weapon_length(150)|swing_damage(48 , cut) | thrust_damage(25 ,  pierce),imodbits_axe ],

["cossack_machete","Cossack machete", [("polyak_sablya_d",0),("polyak_sablya_d_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.2)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(38 , cut) | thrust_damage(33 ,  pierce),imodbits_sword_high ],

["cossack_cavalry_knife","Cossack cavalry knife", [("khergit_sword_two_handed_b",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 
210 , weight(1.2)|difficulty(0)|spd_rtng(95) | weapon_length(100)|swing_damage(36 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ],

["cossack_cavalry_knife_officer","Cossack cavalry knife officer", [("scimitar_b",0),("scab_scimeter_b",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 
210 , weight(1.2)|difficulty(0)|spd_rtng(95) | weapon_length(100)|swing_damage(36 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ],

["berdish", "Pole-axe", [("berdish",0)], itp_type_polearm|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 
 2650 , weight(2.25)|difficulty(11)|spd_rtng(83) | weapon_length(120)|swing_damage(45 , cut) | thrust_damage(23 ,  pierce),imodbits_axe ],

# Prussia
#Tesak_black_scabbard
["russian_briquet_1807_black","Sabre Briquet", [("Russian_briquet_1807",0),("Tesak_black_blackbelt_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(95) | weapon_length(63)|swing_damage(22 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
 ["russian_briquet_1807_black_blackbelt","Sabre Briquet", [("Russian_briquet_1807",0),("Tesak_black_blackbelt_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(95) | weapon_length(63)|swing_damage(22 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
 ["russian_briquet_1807_landwehr","Sabre Briquet", [("Russian_briquet_1807",0),("Tesak_black_blackbelt_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(95) | weapon_length(63)|swing_damage(22 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
 ["russian_peasant_axe_landwehr", "Hand Axe", [("Russian_peasant_axe",0)],#,("Axe_landwehr_scabbard",ixmesh_carry)],
 itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_axe_left_hip, #itcf_carry_sword_left_hip, #|itcf_show_holster_when_drawn,
 80,weight(0)|difficulty(9)|spd_rtng(90) | weapon_length(50)|swing_damage(33 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],#patch1115 56/1
["scottish_sword","Light cavalry sword", [("scottish_sword",0),("scottish_sword_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(95) | weapon_length(63)|swing_damage(22 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],

["maquahuitl","Light cavalry sword", [("maquahuitl",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 
210 , weight(0)|difficulty(0)|spd_rtng(90) | weapon_length(70)|swing_damage(30 , cut) | thrust_damage(15 ,  pierce),imodbits_sword_high ],

["16tchui01","Inca war stick", [("16tchui01",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 
210 , weight(0)|difficulty(0)|spd_rtng(90) | weapon_length(75)|swing_damage(38 , cut) | thrust_damage(12 ,  pierce),imodbits_sword_high ],

["machete","machete", [("turk_sablya_b",0),("turk_sablya_b_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(95) | weapon_length(63)|swing_damage(38 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],

["machete_officer","machete_officer", [("turk_sablya_d",0),("turk_sablya_d_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(95) | weapon_length(63)|swing_damage(38 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],

["damascus_steel_machete","Damascus steel machete", [("seljuksword4",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 
210 , weight(0)|difficulty(0)|spd_rtng(95) | weapon_length(80)|swing_damage(42 , cut) | thrust_damage(23 ,  pierce),imodbits_sword_high ],

["pirate_tomahawk","Pirate tomahawk", [("balta2",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip, 
210 , weight(1.2)|difficulty(0)|spd_rtng(80) | weapon_length(80)|swing_damage(41 , cut) | thrust_damage(15 ,  pierce),imodbits_sword_high ],



#training weapons
["training_officer_sword","Officer Training Sword", [("training_officer_sword",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_attack|itp_wooden_parry, itc_longsword|itcf_carry_sword_left_hip,
210 , weight(1.5)|difficulty(0)|spd_rtng(95)|weapon_length(100)|swing_damage(32, cut)|thrust_damage(29, pierce),imodbits_sword_high ],
 ["training_heavy_sword","Heavy Training Sword", [("training_heavy_sword",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_attack|itp_wooden_parry, itc_longsword|itcf_carry_sword_left_hip,
210 , weight(3.0)|difficulty(0)|spd_rtng(91)|weapon_length(111)|swing_damage(36, cut)|thrust_damage(32, pierce),imodbits_sword_high ],
["training_light_sabre","Light Training Sabre", [("training_light_sabre",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_wooden_attack|itp_wooden_parry, itc_longsword|itcf_carry_sword_left_hip,
210 , weight(2.0)|difficulty(0)|spd_rtng(93)|weapon_length(102)|swing_damage(33, cut)|thrust_damage(30, pierce),imodbits_sword_high ],
#end training weapons

# fake stuff for stupid bots
 ["french_briquet_garde_fake","Sabre Briquet", [("Garde_briquet",0),("Guard_briquet_in_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(1) | weapon_length(1)|swing_damage(1 , cut) | thrust_damage(1 ,  pierce),imodbits_sword_high ],
 ["french_briquet_fake","Sabre Briquet", [("Sabre_briquet_french",0),("sabre_briquetscab",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(1) | weapon_length(1)|swing_damage(1 , cut) | thrust_damage(1 ,  pierce),imodbits_sword_high ],
 ["russian_briquet_1807_fake","Sabre Briquet", [("Russian_briquet_1807",0),("Tesak_black_blackbelt_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(1) | weapon_length(1)|swing_damage(1 , cut) | thrust_damage(1 ,  pierce),imodbits_sword_high ],
 ["russian_briquet_1807_black_fake","Sabre Briquet", [("Russian_briquet_1807",0),("Tesak_black_blackbelt_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(1) | weapon_length(1)|swing_damage(1 , cut) | thrust_damage(1 ,  pierce),imodbits_sword_high ],
 ["russian_briquet_1807_black_blackbelt_fake","Sabre Briquet", [("Russian_briquet_1807",0),("Tesak_black_blackbelt_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(1) | weapon_length(1)|swing_damage(1 , cut) | thrust_damage(1 ,  pierce),imodbits_sword_high ],
 ["russian_briquet_1807_landwehr_fake","Sabre Briquet", [("Russian_briquet_1807",0),("Tesak_black_blackbelt_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(1) | weapon_length(1)|swing_damage(1 , cut) | thrust_damage(1 ,  pierce),imodbits_sword_high ],
 ["russian_peasant_axe_landwehr_fake", "Hand Axe", [("Russian_peasant_axe",0)],#("Axe_landwehr_scabbard",ixmesh_carry)],
 itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_parry, itc_scimitar|itcf_carry_sword_left_hip, #|itcf_show_holster_when_drawn,
87 , weight(0)|difficulty(0)|spd_rtng(1) | weapon_length(1)|swing_damage(1 , cut) | thrust_damage(1 ,  pierce),imodbits_axe ],
 ["austrian_infantry_briquet_fake","Sword Bayonet", [("Austrian_infantry_briquet",0),("Austrian_infantry_briquet_black_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(0)|difficulty(0)|spd_rtng(1) | weapon_length(1)|swing_damage(1 , cut) | thrust_damage(1 ,  pierce),imodbits_sword_high ],
 

# admin toy
["banhammer", "Banhammer", [("ban_hammer",0)], itp_crush_through|itp_type_polearm|itp_offset_lance|itp_can_knock_down| itp_primary|itp_two_handed|itp_wooden_parry, itc_nodachi,
 169 , weight(10)|difficulty(0)|spd_rtng(86) | weapon_length(170)|swing_damage(250 , blunt) | thrust_damage(250 ,  blunt),imodbits_polearm ],


# Instruments
 ["drumstick_right","Drum", [("drumstick_right",0)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary|itp_no_pick_up_from_ground, itcf_carry_quiver_right_vertical, #patch1115 45/1 begin
210 , weight(1.5)|difficulty(0)|spd_rtng(93) | weapon_length(102)|swing_damage(3 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
 ["flute","Flute", [("mm_fife",0)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary|itp_no_pick_up_from_ground, itcf_carry_quiver_front_right, 
210 , weight(1.5)|difficulty(0)|spd_rtng(93) | weapon_length(102)|swing_damage(3 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
 ["horn","Horn", [("horn",0)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary|itp_no_pick_up_from_ground, itcf_carry_sword_left_hip, 
210 , weight(1.5)|difficulty(0)|spd_rtng(93) | weapon_length(102)|swing_damage(3 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
 ["trumpet","Trumpet", [("trumpet",0)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary|itp_no_pick_up_from_ground, itcf_carry_sword_left_hip, 
210 , weight(1.5)|difficulty(0)|spd_rtng(93) | weapon_length(102)|swing_damage(3 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
 ["bugle","Bugle", [("bugle",0)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary|itp_no_pick_up_from_ground, itcf_carry_sword_left_hip, 
210 , weight(1.5)|difficulty(0)|spd_rtng(93) | weapon_length(102)|swing_damage(3 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],
 ["bagpipe","Bagpipes", [("mm_invisible",0)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary|itp_no_pick_up_from_ground, itcf_carry_sword_left_hip, 
210 , weight(1.5)|difficulty(0)|spd_rtng(93) | weapon_length(102)|swing_damage(3 , cut) | thrust_damage(20 ,  pierce),imodbits_sword_high ],  #patch1115 45/1 end

 #弹药
 #Ammo
["bullets","Cartridges", [("cartridge_box_mesh",0),("bullet_projectile",ixmesh_flying_ammo),("cartridge_a",ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_default_ammo|itp_can_penetrate_shield, 0, 64,weight(2.0)|abundance(100)|weapon_length(1)|thrust_damage(1,pierce)|max_ammo(18),imodbits_missile,
 [(ti_on_missile_hit, [(copy_position,pos63,pos1),(store_trigger_param_2, ":collision_type"),(call_script, "script_mm_on_bullet_hit",":collision_type")])]],
["pistol_ammo","Pistol Cartridges", [("cartridge_box_mesh",0),("bullet_projectile",ixmesh_flying_ammo),("bag_ppb1",ixmesh_carry)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield,0, 200,weight(1.0)|abundance(100)|weapon_length(1)|thrust_damage(1,pierce)|max_ammo(12),imodbits_missile,
 [(ti_on_missile_hit, [(copy_position,pos63,pos1),(store_trigger_param_2, ":collision_type"),(call_script, "script_mm_on_bullet_hit",":collision_type")])]],


["bullets_invisible","Cartridges", [("none",0),("bullet_projectile",ixmesh_flying_ammo),("none",ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_default_ammo|itp_can_penetrate_shield, itcf_carry_quiver_back, 64,weight(2.0)|abundance(100)|weapon_length(1)|thrust_damage(1,pierce)|max_ammo(18),imodbits_missile,
 [(ti_on_missile_hit, [(copy_position,pos63,pos1),(store_trigger_param_2, ":collision_type"),(call_script, "script_mm_on_bullet_hit",":collision_type")])]],

["matchlockbullets2","Cartridges", [("bag_ppb1",0),("bullet_projectile",ixmesh_flying_ammo),("bag_ppb1",ixmesh_carry)], itp_type_bullets|itp_merchandise|itp_can_penetrate_shield,itcf_carry_quiver_back, 200,weight(1.0)|abundance(100)|weapon_length(1)|thrust_damage(1,pierce)|max_ammo(12),imodbits_missile,
 [(ti_on_missile_hit, [(copy_position,pos63,pos1),(store_trigger_param_2, ":collision_type"),(call_script, "script_mm_on_bullet_hit",":collision_type")])]],

["arrowswithblackpowder","Rocket Arrows", [("amazon_quiver_new",0),("firearrow",ixmesh_flying_ammo),("amazon_quiver_new",ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_default_ammo|itp_can_penetrate_shield, itcf_carry_quiver_back_right, 64,weight(2.0)|abundance(100)|weapon_length(1)|thrust_damage(1,pierce)|max_ammo(5),imodbits_missile],

["throwing_spears","Throwing Spears", [("jarid_new_b",0),("jarid_new_b_bag", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_next_item_as_melee ,itcf_throw_javelin|itcf_carry_quiver_back|itcf_show_holster_when_drawn, 
525 , weight(3)|difficulty(0)|spd_rtng(87) | shoot_speed(22) | thrust_damage(44 ,  pierce)|max_ammo(4)|weapon_length(65),imodbits_thrown ],
["throwing_spear_melee",         "Throwing Spear", [("jarid_new_b",0),("javelins_quiver", ixmesh_carry)],itp_type_polearm|itp_primary|itp_wooden_parry , itc_spear, 
525 , weight(1)|difficulty(0)|spd_rtng(91) | swing_damage(18, cut) | thrust_damage(23 ,  pierce)|weapon_length(75),imodbits_thrown ],

["matchlockbullets","Cartridges", [("mm_invisible",0),("bullet_projectile",ixmesh_flying_ammo),("bag_a",ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_default_ammo|itp_can_penetrate_shield,itcf_carry_quiver_back|itp_no_pick_up_from_ground, 64,weight(2.0)|abundance(100)|weapon_length(1)|thrust_damage(20,pierce)|max_ammo(12),imodbits_missile,
 [(ti_on_missile_hit, [(copy_position,pos63,pos1),(store_trigger_param_2, ":collision_type"),(call_script, "script_mm_on_bullet_hit",":collision_type")])]],

["jap_arrows", "War_Arrows", [("gf_arrow_3", 0), ("gf_arrow_3_flying", ixmesh_flying_ammo), ("gf_quiver_3", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
410, weight(3)|weapon_length(95)|abundance(50)|thrust_damage(35, cut)|max_ammo(23), imodbits_missile, [] ],

#Only called in scripts 
["canister_ammo","Cartridges", [("bullet_projectile",0),("bullet_projectile",ixmesh_flying_ammo)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield, 0, 64,weight(2.0)|abundance(100)|weapon_length(1)|thrust_damage(100,pierce)|max_ammo(1),imodbits_missile,
 [(ti_on_missile_hit, [(copy_position,pos63,pos1),(store_trigger_param_2, ":collision_type"),(call_script, "script_mm_on_bullet_hit",":collision_type")])]],
["shell_fragment","Shell Fragments", [("bullet_projectile",0),("prtcl_dust_e",ixmesh_flying_ammo)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield, 0, 64,weight(2.0)|abundance(100)|weapon_length(3)|thrust_damage(500,pierce)|max_ammo(1),imodbits_missile,
 [(ti_on_missile_hit, [(copy_position,pos63,pos1),(store_trigger_param_2, ":collision_type"),(call_script, "script_mm_on_bullet_hit",":collision_type")])]],



 #Cheat
 ["explosive_bullets","Cartridges", [("rocket",0),("rocket",ixmesh_flying_ammo)], itp_type_bolts|itp_ignore_gravity|itp_ignore_friction|itp_can_penetrate_shield, 0, 64,weight(2.0)|abundance(100)|weapon_length(100)|thrust_damage(100,pierce)|max_ammo(120),imodbits_missile,
 [
  (ti_on_missile_hit,
  [
    (this_or_next|multiplayer_is_server),
    (neg|game_in_multiplayer_mode),
    (store_trigger_param_1, ":thrower_agent"),
    #pos1 - Missile hit position
    (copy_position,pos47,pos1),
    (call_script,"script_explosion_at_position",":thrower_agent",500,500), # Input: shooter_agent_no, max_damage points, range in cm
   ]),]],
 
# cannon ammo
["cannon_cartridge_round", "Round Shot", [("cannonball_cartridge",0)], itp_type_thrown |itp_merchandise,0,
 360, weight(5)|difficulty(0)|spd_rtng(70) | shoot_speed(0) | thrust_damage(1,blunt)|max_ammo(1)|weapon_length(5),imodbits_none],
["cannon_cartridge_shell", "Shell (Explosive)", [("bomb_cartridge",0)], itp_type_thrown |itp_merchandise,0,
 360, weight(5)|difficulty(0)|spd_rtng(70) | shoot_speed(0) | thrust_damage(1,blunt)|max_ammo(1)|weapon_length(5),imodbits_none],
["cannon_cartridge_canister", "Canister Shot", [("canister_cartridge",0)], itp_type_thrown |itp_merchandise,0,
 360, weight(5)|difficulty(0)|spd_rtng(70) | shoot_speed(0) | thrust_damage(1,blunt)|max_ammo(1)|weapon_length(5),imodbits_none],
["cannon_cartridge_bomb", "Mortar Bomb", [("mortar_cartdridge",0)], itp_type_thrown |itp_merchandise,0,
 360, weight(5)|difficulty(0)|spd_rtng(70) | shoot_speed(0) | thrust_damage(1,blunt)|max_ammo(1)|weapon_length(5),imodbits_none],
["rockets", "Rockets", [("rocket",0)], itp_type_thrown |itp_merchandise,0,
 360, weight(5)|difficulty(0)|spd_rtng(70) | shoot_speed(0) | thrust_damage(1,blunt)|max_ammo(100)|weapon_length(5),imodbits_none],
["new_rockets", "Rocket Pack", [("cannonball_cartridge",0)], itp_type_thrown |itp_merchandise,0,
 360, weight(5)|difficulty(0)|spd_rtng(70) | shoot_speed(0) | thrust_damage(1,blunt)|max_ammo(1)|weapon_length(5),imodbits_none],
 
 
 #骑枪
 #Lances and other polearms
#French
["french_lance", "Ming Banner(Dragoon)", [("DaMing_banner03",0)],  itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 180 , weight(7.0)|difficulty(0)|spd_rtng(80) | weapon_length(320)|swing_damage(25 ,  cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],

["ming_banner1", "Ming Banner(Dragoon)", [("mingjunqi1",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 180 , weight(7.0)|difficulty(0)|spd_rtng(80) | weapon_length(320)|swing_damage(25 ,  cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],

["ming_banner2", "Ming Banner(Character)", [("mingjunqi2",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 180 , weight(7.0)|difficulty(0)|spd_rtng(80) | weapon_length(320)|swing_damage(25 ,  cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],

["ming_banner3", "Ming Banner(Character)", [("mingjunqi3",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 180 , weight(7.0)|difficulty(0)|spd_rtng(80) | weapon_length(320)|swing_damage(25 ,  cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],

["ming_banner4", "Ming Banner(Character)", [("mingjunqi4",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 180 , weight(7.0)|difficulty(0)|spd_rtng(80) | weapon_length(320)|swing_damage(25 ,  cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],
 
["ming_banner5", "Ming Banner(Character)", [("mingjunqi5",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 180 , weight(7.0)|difficulty(0)|spd_rtng(80) | weapon_length(320)|swing_damage(25 ,  cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],
 
["ming_banner6", "Ming Banner(Character)", [("mingjunqi6",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 180 , weight(7.0)|difficulty(0)|spd_rtng(80) | weapon_length(320)|swing_damage(25 ,  cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],

["ming_banner7", "Ming Banner(Character)", [("mingjunqi7",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 180 , weight(7.0)|difficulty(0)|spd_rtng(80) | weapon_length(320)|swing_damage(25 ,  cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],

["ming_banner8", "Ming Banner(Character)", [("mingjunqi8",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 180 , weight(7.0)|difficulty(0)|spd_rtng(80) | weapon_length(320)|swing_damage(25 ,  cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],

["ming_spear",         "Hongying Spear", [("Txz_hyq",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry|itp_is_pike|itp_no_blur, itc_lance|itcf_carry_spear,
 80 , weight(2.25)|difficulty(0)|spd_rtng(98) | weapon_length(200)|swing_damage(26 , blunt) | thrust_damage(36 ,  pierce),imodbits_polearm ],

["ming_spear2",         "Ming war spear", [("Txz_slq",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry|itp_is_pike|itp_no_blur, itc_lance|itcf_carry_spear,
 80 , weight(2.25)|difficulty(0)|spd_rtng(98) | weapon_length(200)|swing_damage(26 , blunt) | thrust_damage(36 ,  pierce),imodbits_polearm ],

["qing_w_banner", "Qing white Banner", [("junqi_b",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 180 , weight(7.0)|difficulty(0)|spd_rtng(80) | weapon_length(320)|swing_damage(25 ,  cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],
 
["qing_r_banner", "Qing Red Banner", [("junqi_hong",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 180 , weight(7.0)|difficulty(0)|spd_rtng(80) | weapon_length(320)|swing_damage(25 ,  cut) | thrust_damage(30 ,  pierce),imodbits_polearm ], 

["qing_y_banner", "Qing Yellow Banner", [("junqi_huang",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 180 , weight(7.0)|difficulty(0)|spd_rtng(80) | weapon_length(320)|swing_damage(25 ,  cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],
 
["qing_b_banner", "Qing Blue Banner", [("junqi_lan",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 180 , weight(7.0)|difficulty(0)|spd_rtng(80) | weapon_length(320)|swing_damage(25 ,  cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],

["qing_xw_banner", "Qing Subwhite Banner", [("junqi_xb",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 180 , weight(7.0)|difficulty(0)|spd_rtng(80) | weapon_length(320)|swing_damage(25 ,  cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],
 
["qing_xr_banner", "Qing Subred Banner", [("junqi_xhong",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 180 , weight(7.0)|difficulty(0)|spd_rtng(80) | weapon_length(320)|swing_damage(25 ,  cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],


["qing_xy_banner", "Qing Subyellow Banner", [("junqi_xhuang",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 180 , weight(7.0)|difficulty(0)|spd_rtng(80) | weapon_length(320)|swing_damage(25 ,  cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],
 
 
["qing_xb_banner", "Qing Blue Banner", [("junqi_xlan",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 180 , weight(7.0)|difficulty(0)|spd_rtng(80) | weapon_length(320)|swing_damage(25 ,  cut) | thrust_damage(30 ,  pierce),imodbits_polearm ],

["oda_colour","Oda Colour", [("gekokujo_sashimono_oda_2",0)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],

["dane_colour","Dane Colour", [("gekokujo_sashimono_date_2",0)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],

["shimazu_colour","Shimazu Colour", [("gekokujo_sashimono_shimazu_2",0)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],

["chosokabe_colour","chosokabe Colour", [("gekokujo_sashimono_chosokabe_2",0)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],

["takeda_colour","Takeda Colour", [("gekokujo_sashimono_takeda_2",0)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itcf_carry_spear|itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],

#Prussian
["prussian_lance", "Lance", [("lance_prussia",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance|itp_no_parry| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itc_lance,
 180 , weight(2.5)|difficulty(0)|spd_rtng(76) | weapon_length(185)|swing_damage(25 ,  pierce) | thrust_damage(30 ,  pierce),imodbits_polearm ],

#Austrian
["austrian_lance", "Lance", [("lance_austria",0)],itp_has_upper_stab| itp_couchable|itp_type_polearm|itp_offset_lance|itp_no_parry| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itc_lance,
 180 , weight(2.5)|difficulty(0)|spd_rtng(76) | weapon_length(185)|swing_damage(25 ,  pierce) | thrust_damage(30 ,  pierce),imodbits_polearm ], 
 
#Rhine
["saxon_lance", "Lance", [("saxon_ulan_pike",0)],itp_has_upper_stab| itp_couchable|itp_type_polearm|itp_offset_lance|itp_no_parry| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itc_lance,
 180 , weight(2.5)|difficulty(0)|spd_rtng(76) | weapon_length(185)|swing_damage(25 ,  pierce) | thrust_damage(30 ,  pierce),imodbits_polearm ], 
 
#Russian
["russian_cossack_pike", "Lance", [("Russian_cossack_pike",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance|itp_no_parry| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itc_lance,
 180 , weight(2.5)|difficulty(0)|spd_rtng(76) | weapon_length(185)|swing_damage(25 ,  pierce) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["russian_lancer_pike", "Lance", [("Russian_lancer_pike",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance|itp_no_parry| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itc_lance,
 180 , weight(2.5)|difficulty(0)|spd_rtng(76) | weapon_length(185)|swing_damage(25 ,  pierce) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["russian_opolcheniye_pike","Pike", [("Txz_slq",0)], itp_has_upper_stab|itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_is_pike|itp_no_blur, itc_spear,
 125 , weight(3.0)|difficulty(0)|spd_rtng(70) | weapon_length(188)|swing_damage(0 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["russian_peasant_kosa", "Scythe", [("Russian_peasant_kosa",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_is_pike|itp_no_blur, itc_staff,
 125 , weight(2.7)|difficulty(0)|spd_rtng(70) | weapon_length(170)|swing_damage(20 , cut) | thrust_damage(20, pierce),imodbits_polearm ],
["russian_peasant_fork", "Wooden Fork", [("Russian_peasant_fork",0)], itp_has_upper_stab|itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_is_pike|itp_no_blur, itc_spear,
 125 , weight(2.7)|difficulty(0)|spd_rtng(75) | weapon_length(145)|swing_damage(6 , blunt) | thrust_damage(25, pierce),imodbits_polearm ],
["russian_peasant_pitchfork", "Pitchfork", [("Russian_peasant_pitchfork",0)], itp_has_upper_stab|itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itc_spear,
 125 , weight(2.7)|difficulty(0)|spd_rtng(75) | weapon_length(145)|swing_damage(6 , blunt) | thrust_damage(25, pierce),imodbits_polearm ],
["russian_peasant_sap", "Rake", [("Russian_peasant_sap",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_no_blur, itc_guandao2,
 125 , weight(2.7)|difficulty(0)|spd_rtng(75) | weapon_length(119)|swing_damage(18 , pierce) | thrust_damage(5, blunt),imodbits_polearm ],

["sap", "Hoe", [("kuwa",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_no_blur, itc_guandao2,
 125 , weight(2.7)|difficulty(0)|spd_rtng(75) | weapon_length(125)|swing_damage(18 , pierce) | thrust_damage(5, blunt),imodbits_polearm ],
 
["birch_trunk", "Birch Trunk", [("Birch_trunk",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_crush_through|itp_can_knock_down|itp_unbalanced|itp_no_blur, itc_parry_polearm|itc_cut_two_handed|itcf_thrust_polearm,
 125 , weight(10.0)|difficulty(0)|spd_rtng(67) | weapon_length(104)|swing_damage(30 , blunt) | thrust_damage(8, blunt),imodbits_polearm ], #patch1115 24/1
["russian_peasant_kosa2", "Scythe", [("Russian_peasant_kosa2",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_no_blur, itc_parry_polearm|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm,
 125 , weight(2.7)|difficulty(0)|spd_rtng(74) | weapon_length(115)|swing_damage(25 , cut) | thrust_damage(0, pierce),imodbits_polearm ],
["russian_peasant_club","Club", [("Russian_peasant_club",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_can_knock_down|itp_no_blur, itc_parry_polearm|itc_cut_two_handed|itcf_thrust_polearm,
 125 , weight(3.3)|difficulty(0)|spd_rtng(70) | weapon_length(90)|swing_damage(20 , blunt) | thrust_damage(5, blunt),imodbits_polearm ],
["russian_peasant_birch_club","Birch Club", [("Russian_peasant_birch_club",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_can_knock_down|itp_no_blur, itc_parry_polearm|itc_cut_two_handed|itcf_thrust_polearm,
 125 , weight(3.3)|difficulty(0)|spd_rtng(70) | weapon_length(90)|swing_damage(20 , blunt) | thrust_damage(5, blunt),imodbits_polearm ],
["russian_peasant_pike","Pike", [("Russian_peasant_pike",0)], itp_has_upper_stab|itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_no_parry|itp_two_handed|itp_is_pike|itp_no_blur, itc_lance,
 125 , weight(3.0)|difficulty(0)|spd_rtng(70) | weapon_length(258)|swing_damage(0 , blunt) | thrust_damage(30 ,  pierce),imodbits_polearm ],
["russian_peasant_kuvalda", "Sledgehammer", [("Russian_peasant_kuvalda",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_no_blur, itc_parry_polearm|itc_cut_two_handed,
 125 , weight(2.7)|difficulty(0)|spd_rtng(75) | weapon_length(64)|swing_damage(30 , blunt) | thrust_damage(5, blunt),imodbits_polearm ],
["russian_peasant_2handed_axe", "Lumber Axe", [("Russian_peasant_2handed_axe",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_no_blur, itc_parry_polearm|itc_cut_two_handed,
 125 , weight(2.7)|difficulty(0)|spd_rtng(70) | weapon_length(64)|swing_damage(35 , cut) | thrust_damage(0, pierce),imodbits_polearm ],
["russian_peasant_rogatina", "Hunting Spear", [("Russian_peasant_rogatina",0)], itp_has_upper_stab|itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_is_pike|itp_no_blur, itc_lance,
 125 , weight(2.7)|difficulty(0)|spd_rtng(75) | weapon_length(159)|swing_damage(6 , blunt) | thrust_damage(25, pierce),imodbits_polearm ],
["sapper_axe_ship", "Axe", [("sapper_axe",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_bonus_against_shield, itc_cut_two_handed|itc_parry_polearm|itcf_carry_axe_back,
 125 , weight(2.7)|difficulty(0)|spd_rtng(70) | weapon_length(73)|swing_damage(40 , cut) | thrust_damage(0, pierce),imodbits_polearm ],
["sapper_axe_rus_ship", "Axe", [("Russian_sappeur_axe",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_bonus_against_shield, itc_cut_two_handed|itc_parry_polearm|itcf_carry_axe_back,
 125 , weight(2.7)|difficulty(0)|spd_rtng(70) | weapon_length(58)|swing_damage(40 , cut) | thrust_damage(0, pierce),imodbits_polearm ],

 #weapons for GF mode. #patch1115 60/12
["french_mousquiton_melee_gf", "Cavalry Carbine", [("french_mousquiton",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket,itc_musket_melee|itcf_carry_spear,
180 , weight(0)|difficulty(0)|spd_rtng(86) | weapon_length(76)|swing_damage(23 , blunt) | thrust_damage(12,  blunt),imodbits_none ],

["french_mousquiton_light_melee_gf", "Light Cavalry Carbine", [("french_mousquiton_light",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket,itc_musket_melee|itcf_carry_spear,
180 , weight(0)|difficulty(0)|spd_rtng(86) | weapon_length(76)|swing_damage(23 , blunt) | thrust_damage(12,  blunt),imodbits_none ],

["french_dragoon_musket_melee_gf", "Cavalry Musket", [("french_dragoon_musket",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket,itc_musket_melee|itcf_carry_spear,
180 , weight(0)|difficulty(0)|spd_rtng(86) | weapon_length(115)|swing_damage(20 , blunt) | thrust_damage(12,  blunt),imodbits_none ],

["russian_dragoon_musket_melee_gf", "Cavalry Musket", [("Russian_dragoon_musket",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket,itc_musket_melee|itcf_carry_spear,
180 , weight(0)|difficulty(0)|spd_rtng(86) | weapon_length(115)|swing_damage(20 , blunt) | thrust_damage(12,  blunt),imodbits_none ],

["russian_gusarskiy_karabin_melee_gf", "Musketoon", [("Russian_gusarskiy_karabin",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket,itc_musket_melee|itcf_carry_spear,
180 , weight(0)|difficulty(0)|spd_rtng(86) | weapon_length(58)|swing_damage(22 , blunt) | thrust_damage(12,  blunt),imodbits_none ],

["british_carbine_melee_gf", "Cavalry Carbine", [("paget_carabine",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket,itc_musket_melee|itcf_carry_spear,
180 , weight(0)|difficulty(0)|spd_rtng(86) | weapon_length(50)|swing_damage(23 , blunt) | thrust_damage(12,  blunt),imodbits_none ],

["russian_rifle_1805_melee_gf", "Rifle", [("Russian_rifle_1805",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket|itp_can_knock_down,itc_musket_melee|itcf_carry_spear,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(74)|swing_damage(23 , blunt) | thrust_damage(22 ,  blunt),imodbits_none ],

["british_baker_rifle_melee_gf", "Rifle", [("baker_rifle",0)], itp_has_upper_stab|itp_type_polearm |itp_primary|itp_no_blur|itp_offset_musket|itp_can_knock_down,itc_musket_melee|itcf_carry_spear,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(85)|swing_damage(23 , blunt) | thrust_damage(22 ,  blunt),imodbits_none ],

["french_charleville_melee_gf", "Infantry Musket", [("french_charleville",0)], itp_cant_use_on_horseback|itp_has_upper_stab|itp_type_polearm |itp_primary|itp_is_pike|itp_no_blur,itc_spear|itcf_carry_spear,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(138)|swing_damage(40 ,  pierce) | thrust_damage(45 ,  pierce),imodbits_none ],

["french_versailles_melee_gf", "Infantry Musket", [("french_versailles",0)], itp_cant_use_on_horseback|itp_has_upper_stab|itp_type_polearm |itp_primary|itp_is_pike|itp_no_blur,itc_spear|itcf_carry_spear,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(138)|swing_damage(40 ,  pierce) | thrust_damage(45 ,  pierce),imodbits_none ], 

["british_brown_bess_melee_gf", "Infantry Musket", [("brown_bess_musket",0)], itp_cant_use_on_horseback|itp_has_upper_stab|itp_type_polearm |itp_primary|itp_is_pike|itp_no_blur,itc_spear|itcf_carry_spear,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(138)|swing_damage(40 ,  pierce) | thrust_damage(45 ,  pierce),imodbits_none ], 

["russian_musket_1808_melee_gf", "Infantry Musket", [("Russian_musket_1808",0)], itp_cant_use_on_horseback|itp_has_upper_stab|itp_type_polearm |itp_primary|itp_is_pike|itp_no_blur,itc_spear|itcf_carry_spear,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(138)|swing_damage(40 ,  pierce) | thrust_damage(45 ,  pierce),imodbits_none ], 

["austrian_musket_melee_gf", "Infantry Musket", [("austrian_musket",0)], itp_cant_use_on_horseback|itp_has_upper_stab|itp_type_polearm |itp_primary|itp_is_pike|itp_no_blur,itc_spear|itcf_carry_spear,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(138)|swing_damage(40 ,  pierce) | thrust_damage(45 ,  pierce),imodbits_none ], 

["prussian_potsdam_melee_gf", "Infantry Musket", [("potsdam_musket",0)], itp_cant_use_on_horseback|itp_has_upper_stab|itp_type_polearm |itp_primary|itp_is_pike|itp_no_blur,itc_spear|itcf_carry_spear,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(138)|swing_damage(40 ,  pierce) | thrust_damage(45 ,  pierce),imodbits_none ], 

["prussian_musket_1806_melee_gf", "Infantry Musket", [("prussian_kuhfuss",0)], itp_cant_use_on_horseback|itp_has_upper_stab|itp_type_polearm |itp_primary|itp_is_pike|itp_no_blur,itc_spear|itcf_carry_spear,
180 , weight(0)|difficulty(0)|spd_rtng(85) | weapon_length(138)|swing_damage(40 ,  pierce) | thrust_damage(45 ,  pierce),imodbits_none ], 
#end GF maps #patch1115 60/12
#training weapons
["training_musket", "Training Musket", [("training_musket",0)], itp_cant_use_on_horseback|itp_has_upper_stab|itp_type_polearm|itp_primary|itp_is_pike|itp_wooden_attack|itp_wooden_parry|itp_no_blur, itc_spear|itcf_carry_spear,
180, weight(0)|difficulty(0)|spd_rtng(85)|weapon_length(138)|swing_damage(40, pierce)|thrust_damage(45, pierce), imodbits_none ],
#end training weapons

#旗帜
# Flags
#French
["flag_france_45e","French Line Infantry Colour", [("france_colour_45e",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["flag_france_84e","French Line Infantry Colour", [("france_colour_84e",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["flag_france_vistula","Vistula Legion Colour", [("france_colour_vistula",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["flag_france_grenadiers","Oda Colour", [("gekokujo_sashimono_oda_2",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["flag_france_15","French Light Infantry Colour", [("france_colour_15eme",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["flag_france_hussard","French Hussar Colour", [("france_colour_hussards",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(140)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["flag_france_carab","French Carabinier Colour", [("france_colour_lanciers",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(140)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["flag_france_cuirassier","French Cuirassier Colour", [("france_colour_cuirassiers",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(140)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["flag_france_cheval","French Grenadiers a Cheval Colour", [("france_colour_gren_a_cheval",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(140)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["flag_france_dragon","French Dragoon Colour", [("france_colour_dragons",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(140)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["flag_france_lancier","French Lancer Colour", [("france_colour_lanciers",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(140)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
#Russian
["flag_russia_opolcheniye","Russian St Petersburg's Opolcheniye Flag", [("russian_colour_opolcheniye",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["flag_russia_pavlovsk_color","Russian Pavlovskiy Regimental Colour", [("russian_colour_pavlovsk_color",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["flag_russia_pavlovsk_white","Russian Pavlovskiy White Flag", [("russian_colour_pavlovsk_white",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["flag_russia_preobragenskiy_color","Russian Preobrazhenskiy Regimental Colour", [("russian_colour_preobragenskiy_color",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["flag_russia_preobragenskiy_white","Russian Preobrazhenskiy White Flag", [("russian_colour_preobragenskiy_white",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["flag_russia_simbirsk_color","Russian Simbirskiy Regimental Colour", [("russian_colour_simbirsk_color",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["flag_russia_simbirsk_white","Russian Simbirskiy White Flag", [("russian_colour_simbirsk_white",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["flag_russia_kyiv_dragoon","Russian Kyiv Dragoons Guidon", [("russian_colour_kyiv_dragoon",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(140)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
 #British
["britain_colour_33rd_regt","Ming Flag", [("DaMing_banner01",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["britain_colour_33rd_king","British 33rd King's Colour", [("britain_colour_33rd_king",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["britain_colour_42nd_regt","British 42nd Reg. Colour", [("britain_colour_42nd_regt",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["britain_colour_42nd_king","British 42nd King's Colour", [("britain_colour_42nd_king",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["britain_colour_2nd_regt","British 2nd Reg. Colour", [("britain_colour_2nd_king",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["britain_colour_2nd_king","British 2nd King's Colour", [("britain_colour_2nd_regt",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["britain_colour_51st_regt","British 51st Reg. Colour", [("britain_colour_51st_regt",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["britain_colour_51st_king","British 51st King's Colour", [("britain_colour_51st_king",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["britain_colour_kgl_regt","British KGL Reg. Colour", [("britain_colour_kgl_regt",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["britain_colour_kgl_king","British KGL King's Colour", [("britain_colour_kgl_king",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["britain_colour_blues","British Horse Guards Colour", [("britain_colour_blues",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(140)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
 #Prussian
["prussia_colour_infantry","Prussian Infantry Colour", [("flag_prussia_infantry",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["prussia_colour_infantry2","Prussian Infantry Colour", [("flag_prussia_infantry2",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["prussia_colour_guard","Prussian Guard Infantry Colour", [("flag_prussia_guard",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["prussia_colour_landwehr","Prussian Landwehr Colour", [("flag_prussia_landwehr",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["prussia_colour_hussard","Prussian Hussar Colour", [("flag_prussia_hussard",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(140)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
 #Austrian
["austria_colour_leibfahne","Austrian Leibfahne", [("austria_colour_leibfahne",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["austria_colour_ordinarfahne","Austrian Ordinarfahne", [("austria_colour_ordinarfahne",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["austria_colour_ordinarfahne_cav","Austrian Ordinarfahne", [("austria_colour_ordinarfahne_cav",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(140)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
 #Rhine
["bavarian_flag_national","Bavarian National Colour", [("bavarian_flag_national",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["bavarian_flag_regimental","Bavarian Reg. Colour", [("bavarian_flag_regimental",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["saxon_flag_infantry","Saxon Infantry Colour", [("saxon_infantry_flag",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["saxon_flag_uhlan","Saxon Uhlan Standard", [("saxon_ulan_standard",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(140)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["hessian_flag_infantry","Hessian Infantry Colour", [("hessen_infantry_flag",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["westphalian_flag_infantry","Westphalian Infantry Colour", [("west_gr_flag",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["baden_flag_dragoon","Baden Dragoon Standard", [("baden_dragoons_standard",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(140)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["westphalian_flag_cuirassier","Westphalian Cuirassier Standard", [("westphalian_cuirassier_standard",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(140)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["saxon_flag_garde","Saxon Garde du Corps Standard", [("standart_garde_du_corps",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(140)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["wurttemberg_flag_infantry","Wurttemberg Infantry Colour", [("wurttemberg_infantry_flag",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["wurttemberg_flag_infantry2","Wurttemberg Infantry Colour", [("wurttemberg_grenadiers_flag",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],

#Poland
["poland_flag","Polish Colour", [("guoqi",0), ("mesh_banner_f21", ixmesh_inventory)],itp_type_two_handed_wpn|itp_two_handed|itp_wooden_parry|itp_primary, itc_parry_polearm,
 390 , weight(0.5)|difficulty(0)|spd_rtng(50) | weapon_length(320)|swing_damage(1 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],


["ming_arrows2","Ming_Arrows", [("DaMing_arrow",0),("DaMing_arrow",ixmesh_flying_ammo),("DaMing_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
683 , weight(3.0)|weapon_length(91)|thrust_damage(35,cut)|max_ammo(23),imodbits_none,[]],

["qing_arrows2","Qing_Arrows", [("DaMing_arrow",0),("DaMing_arrow",ixmesh_flying_ammo),("arrows_a_kolchan_I", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
683 , weight(3.0)|weapon_length(91)|thrust_damage(35,cut)|max_ammo(23),imodbits_none,[]],

["qing_arrows2_fire","Qing_Arrows(Fire)", [("amazon_arrow",0),("firearrow",ixmesh_flying_ammo),("amazon_quiver_new", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
683 , weight(3.0)|weapon_length(91)|thrust_damage(40,cut)|max_ammo(18),imodbits_none,[    ]], 

#炮兵工具
# Artillery tools
["cannon_lighter","Cannon Lighter", [("lighter",0)], itp_has_upper_stab|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_lance|itcf_carry_bow_back,
210 , weight(1.6)|difficulty(0)|spd_rtng(81) | weapon_length(200)|swing_damage(10 , blunt) | thrust_damage(25 ,  pierce),imodbits_polearm ],
["ramrod", "Ramrod", [("ramrod",0)], itp_has_upper_stab|itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itc_spear|itcf_carry_spear,
 85 , weight(3.0)|difficulty(0)|spd_rtng(81) | weapon_length(135)|swing_damage(10 , blunt) | thrust_damage(12 ,  blunt),imodbits_polearm ],
["rocket_placement", "Rocket Launcher", [("rocket_launcher_folded",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_wooden_parry, itcf_carry_spear,
 85 , weight(15)|difficulty(0)|spd_rtng(81) | weapon_length(135)|swing_damage(10 , blunt) | thrust_damage(12 ,  blunt),imodbits_polearm ],
#望远镜
#Spyglass
["spyglass","Spyglass", [("spyglass",0), ("spyglass_eq", ixmesh_carry)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary, itcf_carry_revolver_right,  
210 , weight(0)|difficulty(0)|spd_rtng(93) | weapon_length(102)|swing_damage(30 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high],

["smoke_bomb", "Smoke Bombs", [("bomb", 0)], itp_type_thrown|itp_primary, 65536, 1, weight(1)|abundance(100)|difficulty(0)|accuracy(0)|spd_rtng(60)|shoot_speed(10)|max_ammo(3)|thrust_damage(1, blunt)|weapon_length(8), imodbit_cracked|imodbit_bent|imodbit_battered, [
    (ti_on_missile_hit, [
        (this_or_next|multiplayer_is_server),
        (neg|game_in_multiplayer_mode),
	    (init_position, pos60),
	    (position_copy_origin, pos60, pos1), # Copy hit position for the script
	    #(particle_system_burst_no_sync,"psys_smoke",pos1,4000),
        (call_script,"script_multiplayer_server_spawn_particle_at_position","psys_smoke",4000),
    ]),
]], 

#骑枪
#Ming_Lance

["greatming_ji", "GreatMing Ji", [("DaMing_hupiji",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_guandao,
 180 , weight(3.0)|difficulty(0)|spd_rtng(80) | weapon_length(230)|swing_damage(45 ,  cut) | thrust_damage(40 ,  pierce),imodbits_polearm ],

["jap_cav_yari", "Cavalry Yari", [("gekokujo_jumonji_yari_5",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_guandao3,
 180 , weight(3.0)|difficulty(0)|spd_rtng(85) | weapon_length(235)|swing_damage(40 ,  cut) | thrust_damage(35 ,  pierce),imodbits_polearm ],

["greatming_dadao", "GreatMing dadao", [("dadao",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_guandao2,
 180 , weight(3.5)|difficulty(0)|spd_rtng(85) | weapon_length(165)|swing_damage(50 ,  cut) | thrust_damage(40 ,  pierce),imodbits_polearm ],

["cavalry_spear","Cavalry spear", [("spear_f_2_9m",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance2,
 125 , weight(1.5)|difficulty(0)|spd_rtng(80) | weapon_length(175)|swing_damage(20 , blunt) | thrust_damage(37 ,  pierce),imodbits_polearm ],
 
["lance_3","Great Lance", [("lance_3",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 125 , weight(2.5)|difficulty(0)|spd_rtng(80) | weapon_length(250)|swing_damage(20 , blunt) | thrust_damage(37 ,  pierce),imodbits_polearm ],
 
["winged_hassur_lance","Winged Hassur Lance", [("pol_gusar_lansa_a",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 125 , weight(3.5)|difficulty(0)|spd_rtng(75) | weapon_length(400)|swing_damage(20 , blunt) | thrust_damage(32 ,  pierce),imodbits_polearm ],
 
["winged_hassur_lance_break","Broken lance", [("dl",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 125 , weight(1.5)|difficulty(0)|spd_rtng(75) | weapon_length(95)|swing_damage(20 , blunt) | thrust_damage(15 ,  blunt),imodbits_polearm ],
 
["winged_hassur_lance2","Lance", [("pol_gusar_lansa_b",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_lance,
 125 , weight(3.5)|difficulty(0)|spd_rtng(78) | weapon_length(350)|swing_damage(20 , blunt) | thrust_damage(35 ,  pierce),imodbits_polearm ],
 
["lance_3_broken","Great Lance", [("duanqiqiang",0)], itp_has_upper_stab|itp_type_polearm| itp_primary|itp_wooden_parry, itcf_carry_spear|itc_spear,
 125 , weight(1.5)|difficulty(0)|spd_rtng(85) | weapon_length(50)|swing_damage(20 , blunt) | thrust_damage(15 ,  blunt),imodbits_polearm ],
 
 
["sovnya", "Sovnya", [("sovnya",0)], itp_has_upper_stab|itp_couchable|itp_type_polearm|itp_offset_lance| itp_primary|itp_two_handed|itp_penalty_with_shield|itp_wooden_parry|itp_is_pike|itp_no_blur, itcf_carry_spear|itc_guandao,
 1100 , weight(2.5)|difficulty(0)|spd_rtng(79) | weapon_length(150)|swing_damage(45 , cut) | thrust_damage(40 ,  pierce),imodbits_axe ],
 
["nagamaki_2", "Nagamaki", [("gekokujo_nagamaki_2", 0), ("gekokujo_nagamaki_2_scabbard", ixmesh_carry)], itp_type_polearm|itp_merchandise|itp_wooden_parry|itp_two_handed|itp_primary, itcf_thrust_polearm|itcf_overswing_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_horseback_slash_polearm|itcf_parry_forward_polearm|itcf_parry_up_polearm|itcf_parry_right_polearm|itcf_parry_left_polearm|itcf_carry_sword_back,
800, weight(2.75)|weapon_length(142)|difficulty(11)|spd_rtng(96)|abundance(75)|swing_damage(40, cut)|thrust_damage(25, pierce), imod_rusty|imod_chipped|imod_balanced|imod_tempered|imod_masterwork|imod_heavy, [] ],

["nodachi",  "Nodachi", [("gekokujo_nodachi_1",0),("gekokujo_nodachi_1_scabbard",ixmesh_carry)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back|itcf_show_holster_when_drawn, 
920 , weight(4.0)|difficulty(11)|spd_rtng(92) | weapon_length(125)|swing_damage(50 , cut) | thrust_damage(35 ,  pierce),imodbits_axe ],

["maquahuitl_two_handed",  "Nodachi", [("maquahuitl_two_handed",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 
920 , weight(4.0)|difficulty(11)|spd_rtng(92) | weapon_length(125)|swing_damage(55 , cut) | thrust_damage(28 ,  pierce),imodbits_axe ],

["pirate_long_tomahawk",  "Pirate long tomahawk", [("balta3",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary, itc_greatsword|itcf_carry_sword_back, 
920 , weight(4.0)|difficulty(11)|spd_rtng(88) | weapon_length(125)|swing_damage(82 , cut) | thrust_damage(12 ,  pierce),imodbits_axe ],

["russian_chopper","Russian saber", [("polyak_sablya_c",0),("polyak_sablya_c_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.2)|difficulty(0)|spd_rtng(92) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ],
#盾牌
#Shield
["ming_shield", "Ming Shield", [("mingduen",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
 42 , weight(2.5)|shield_width(36)|hit_points(350)|body_armor(22)|spd_rtng(110),imodbits_shield ],

["ming_shield2", "Ming Shield", [("DaMing_tengpai",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
 42 , weight(4.0)|shield_width(36)|hit_points(330)|body_armor(16)|spd_rtng(90),imodbits_shield ],
 
["ming_shield3", "Ming Shield", [("zhongguo_dun",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
 42 , weight(4.5)|shield_width(100)|hit_points(430)|body_armor(10)|spd_rtng(150),imodbits_shield ],
 
["ming_shield4", "Ming Shield", [("zhendun",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
 42 , weight(4.5)|shield_width(100)|hit_points(430)|body_armor(10)|spd_rtng(150),imodbits_shield ],
 
["ming_shield5", "Ming Shield", [("bigshield",0)], itp_type_shield|itp_wooden_parry, itcf_carry_kite_shield,  
 42 , weight(4.5)|shield_width(100)|hit_points(430)|body_armor(10)|spd_rtng(150),imodbits_shield ],

["steel_shield", "Steel_Shield", [("shield_dragon", 0)], itp_type_shield|itp_merchandise, itcf_carry_round_shield, 
697, weight(4)|shield_width(100)|abundance(100)|hit_points(700)|body_armor(17)|spd_rtng(61), imodbits_shield, [] ],

["wooden_shield", "Heavy_Board_Shield", [("mudun", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield, 
400, weight(5.25)|shield_width(100)|abundance(100)|hit_points(430)|body_armor(10)|spd_rtng(78), imodbits_none, [] ],

["aztec_shield", "Heavy_Board_Shield", [("1aztec_shield333", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield, 
400, weight(2.5)|shield_width(100)|abundance(100)|hit_points(430)|body_armor(50)|spd_rtng(78), imodbits_none, [] ],

["inca_giant_shield", "Inca giant shield", [("ca_pavis", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield, 
400, weight(3.5)|shield_width(120)|abundance(100)|hit_points(750)|body_armor(25)|spd_rtng(65), imodbits_none, [] ],

["turkish_shield1", "Turkish shield", [("tarch_a", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield, 
400, weight(3.5)|shield_width(100)|abundance(100)|hit_points(360)|body_armor(15)|spd_rtng(100), imodbits_none, [] ],

["turkish_shield2", "Turkish shield", [("tarch_b", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry|itp_cant_use_on_horseback, itcf_carry_board_shield, 
400, weight(3.5)|shield_width(100)|abundance(100)|hit_points(360)|body_armor(15)|spd_rtng(100), imodbits_none, [] ],

["osman_steel_shield", "Osman steel shield", [("turkish_kalkan_d", 0)], itp_type_shield|itp_merchandise, itcf_carry_board_shield, 
400, weight(4.0)|shield_width(40)|abundance(100)|hit_points(700)|body_armor(30)|spd_rtng(61), imodbits_none, [] ],

["russian_shield", "Russian shield", [("oim_shield_round_a", 0)], itp_type_shield|itp_merchandise|itp_wooden_parry, itcf_carry_board_shield, 
400, weight(4.0)|shield_width(50)|abundance(100)|hit_points(700)|body_armor(30)|spd_rtng(100), imodbits_none, [] ],
#Misc item: Keys
["key", "Key", [("key",0)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary, 0,
210 , weight(0)|difficulty(0)|spd_rtng(93)|weapon_length(102)|swing_damage(30, cut)|thrust_damage(30, pierce), imodbits_sword_high],
["key_gold", "Golden Key", [("key_gold",0)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary, 0,
210 , weight(0)|difficulty(0)|spd_rtng(93)|weapon_length(102)|swing_damage(30, cut)|thrust_damage(30, pierce), imodbits_sword_high],

#Misc item: drinking
["drinking_cup", "Cup", [("drinking_cup_carry",0), ("drinking_cup", ixmesh_carry)], itp_type_two_handed_wpn|itp_wooden_parry|itp_primary, 0,
 210, weight(1)|difficulty(0)|spd_rtng(90)|weapon_length(32)|swing_damage(24, blunt)|thrust_damage(18, blunt), imodbits_sword_high ],
["drinking_tea_cup", "Tea Cup", [("drinking_tea_cup_carry",0), ("drinking_tea_cup", ixmesh_carry)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary, 0,
 210, weight(1)|difficulty(0)|spd_rtng(90)|weapon_length(32)|swing_damage(24, blunt)|thrust_damage(18, blunt), imodbits_sword_high ],
["drinking_tea_cup_plate", "Tea Cup", [("drinking_tea_cup_plate_carry",0), ("drinking_tea_cup_plate", ixmesh_carry)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary, 0,
 210, weight(1.2)|difficulty(0)|spd_rtng(90)|weapon_length(32)|swing_damage(24, blunt)|thrust_damage(18, blunt), imodbits_sword_high ],
#["drinking_tea_plate", "Tea Cup Plate Shield", [("drinking_tea_plate_carry",0), ("drinking_tea_plate", ixmesh_carry)], itp_type_shield|itp_wooden_parry, 0,
 # 210, weight(0.2)|difficulty(0)|spd_rtng(90)|weapon_length(32)|swing_damage(24, blunt)|thrust_damage(18, blunt),imodbits_sword ],
["drinking_bottle", "Bottle", [("drinking_bottle_carry",0), ("drinking_bottle", ixmesh_carry)], itp_type_one_handed_wpn|itp_wooden_parry|itp_primary|itp_next_item_as_melee, 0,
 210, weight(1.2)|difficulty(0)|spd_rtng(90)|weapon_length(32)|swing_damage(24, blunt)|thrust_damage(18, blunt), imodbits_sword_high ],
["drinking_bottle_melee", "Bottle", [("drinking_bottle_carry",0), ("drinking_bottle", ixmesh_carry)], itp_type_one_handed_wpn|itp_primary|itp_no_parry|itp_no_blur|itp_offset_musket, itc_dagger,
 210, weight(1.2)|difficulty(0)|spd_rtng(90)|weapon_length(32)|swing_damage(24, blunt)|thrust_damage(18, blunt), imodbits_sword_high ],

#Misc item: cane
["cane", "Drill Cane", [("drill_cane",0)], itp_type_one_handed_wpn|itp_wooden_parry|itp_wooden_attack|itp_merchandise|itp_primary|itp_next_item_as_melee, 0,
 210, weight(1.0)|difficulty(0)|spd_rtng(95)|weapon_length(90)|swing_damage(10, blunt)|thrust_damage(10, blunt), imodbits_sword_high ],
["cane_melee", "Drill Cane", [("drill_cane",0)], itp_type_one_handed_wpn|itp_wooden_parry|itp_wooden_attack|itp_merchandise|itp_primary, itc_longsword,
 210, weight(1.0)|difficulty(0)|spd_rtng(95)|weapon_length(90)|swing_damage(10, blunt)|thrust_damage(10, blunt), imodbits_sword_high ],

#Bandage # patch1115 surgeon
["bandages","Bandages", [("bandage",0)], itp_type_one_handed_wpn|itp_primary|itp_no_parry, itc_dagger_no_stab|itcf_carry_pistol_front_left, 
210 , weight(1.6)|difficulty(0)|spd_rtng(65) | weapon_length(25)|swing_damage(10 , blunt) | thrust_damage(0 ,  pierce),imodbits_sword_high ],



# Admin Toys
["grenade", "Holy Handgrenade", [("hhg",0)], itp_type_thrown|itp_primary ,itcf_throw_stone, 1 , weight(4)|difficulty(0)|spd_rtng(97) | shoot_speed(30) | thrust_damage(11 ,  blunt)|max_ammo(100)|weapon_length(8),imodbit_large_bag,
[
  (ti_on_weapon_attack, 
  [
    (copy_position,pos56,pos1),
    (call_script,"script_multiplayer_server_play_sound_at_position","snd_holy_call"),
  ]),
  (ti_on_missile_hit,
  [
    (store_trigger_param_1, ":thrower_agent"),
    #pos1 - Missile hit position
    (copy_position,pos47,pos1),
    (call_script,"script_explosion_at_position",":thrower_agent",500,500), # Input: shooter_agent_no, max_damage points, range in cm
   ]),
 ]],
 
#Sapper Items
["sapper_axe", "Sapper Axe", [("sapper_axe",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_bonus_against_shield, itc_cut_two_handed|itc_parry_polearm|itcf_carry_axe_back,
 125 , weight(2.7)|difficulty(0)|spd_rtng(70) | weapon_length(100)|swing_damage(40 , cut) | thrust_damage(0, pierce),imodbits_polearm ],
["sapper_axe_rus", "Sapper Axe", [("Russian_sappeur_axe",0)], itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_bonus_against_shield, itc_cut_two_handed|itc_parry_polearm|itcf_carry_axe_back,
 125 , weight(2.7)|difficulty(0)|spd_rtng(70) | weapon_length(100)|swing_damage(40 , cut) | thrust_damage(0, pierce),imodbits_polearm ],
["construction_hammer", "Construction Hammer", [("sapper_hammer",0)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_primary, itc_scimitar|itcf_carry_quiver_right_vertical, 
 210 , weight(1.5)|difficulty(0)|spd_rtng(92) | weapon_length(120)|swing_damage(4 , blunt) | thrust_damage(0 ,  pierce),imodbits_sword_high ],
["shovel", "Spade", [("shovel",0),("shovel_eq",ixmesh_carry)], itp_has_upper_stab|itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed|itp_next_item_as_melee, itcf_carry_bow_back|itc_parry_polearm | itcf_thrust_onehanded_lance |itcf_thrust_onehanded_lance_horseback | itcf_thrust_polearm,
 125 , weight(2.5)|difficulty(0)|spd_rtng(75) | weapon_length(140)|swing_damage(6 , blunt) | thrust_damage(16, pierce),imodbits_polearm ],
["shovel_undig", "Spade", [("shovel",0)], itp_has_upper_stab|itp_type_polearm|itp_merchandise| itp_cant_use_on_horseback|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_two_handed, itcf_carry_bow_back|itc_parry_polearm | itcf_thrust_onehanded_lance |itcf_thrust_onehanded_lance_horseback | itcf_thrust_polearm,
 125 , weight(2.5)|difficulty(0)|spd_rtng(75) | weapon_length(140)|swing_damage(6 , blunt) | thrust_damage(16, pierce),imodbits_polearm ],
["french_bomb", "Explosives", [("barreltriangulated",0)], itp_type_thrown |itp_merchandise,itcf_throw_stone,
360, weight(5)|difficulty(0)|spd_rtng(70) | shoot_speed(0) | thrust_damage(1,blunt)|max_ammo(1)|weapon_length(5),imodbits_none,[
 (ti_on_missile_hit,
 [
   (store_trigger_param_1, ":user_agent"),
   (call_script, "script_multiplayer_server_construct_prop", ":user_agent", "spr_mm_french_barrel_explosive")
 ])]],
 
 
 #身甲
#Uniforms
 #French
["french_voltigeur_body_officer", "Farmer coat", [("sam_pesant_jap",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_voltigeur_body_ranker", "Farmer coat", [("sam_pesant_jap1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_voltigeur_body_sarge", "Farmer coat", [("sam_pesant_jap2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_45e_body_officer", "Farmer coat", [("sam_pesant_jap3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_45e_body_colours", "Japanese half armor", [("gekokujo_okegawa_half_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(4.5)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["french_45e_body_ranker", "Japanese armor", [("gekokujo_mogami_short_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(7)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["french_84e_body_officer", "Japanese spearman armor", [("gekokujo_mogami_short_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(18)|difficulty(0) ,imodbits_cloth ],
["french_84e_body_ranker", "Japanese spearman armor", [("gekokujo_tatami_short_4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["french_84e_body_sarge", "French Infantry Uniform", [("french_84e_body_flagcarrier",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_dragoon_body_ranker", "Date armor", [("gekokujo_okegawa_short_date",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["dane_armor", "Date armor", [("gekokujo_okegawa_short_date2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["french_dragoon_body_officer", "Date armor", [("gekokujo_yukinoshita_long_12",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(7)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
["french_general_body_boney", "Tokugaiemitsu's Uniform", [("tokugawa_motoyasu",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(7)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
["french_grenadiers_a_cheval_body_colours", "French Horse Grenadier Uniform", [("french_grenadiers_a_cheval_body_flagman",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_grenadiers_a_cheval_body_ranker", "Uma-Yumi Armor", [("gekokujo_kebiki_5",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(7)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["french_grenadiers_a_cheval_body_officer", "Uma-Yumi Armor", [("gekokujo_kebiki_new10",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(7)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
["french_gap_body_colours", "French Grenadier Uniform", [("french_GRaP_body_flagman",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_gap_body_ranker", "Oda armor", [("gekokujo_okegawa_short_oda",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_gap_body_officer", "French Grenadier Uniform", [("french_GRaP_body_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_art_ranker_body", "Otomo Artillery Armor", [("gekokujo_okegawa_short_otomo2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(5)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["french_art_ranker_body_alt", "French Artillery Uniform", [("french_art_ranker_body_alt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_art_officer_body", "Otomo armor", [("gekokujo_mogami_short_5",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["french_vistula_body_ranker", "Samurai armor", [("ggekokujo_okegawa_long_3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6.5)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
["french_vistula_body_colours", "Samurai armor", [("gekokujo_okegawa_long_6",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6.5)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
["french_vistula_body_officer", "Vistula Legion Uniform", [("french_vistula_body_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_lancer_body_ranker", "Monk soldior armor", [("gekokujo_okegawa_short_10",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
["french_lancer_body_colours","Monk soldior armor", [("gekokujo_mogami_short_4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
["french_lancer_body_officer", "French Guard Lancer Uniform", [("french_lancer_officer_body",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_cuirassier_ranker", "Takeda Armor", [("daimyo_okegawa_long_red",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(7)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
["french_cuirassier_colours", "French Cuirassier Uniform", [("fr_cuirassier_body_porte_aigle",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_cuirassier_officer", "French Cuirassier Uniform", [("fr_cuirassier_body_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_carabineer_ranker", "French Carabineer Uniform", [("fr_carabineer_ranker",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_carabineer_colours", "French Carabineer Uniform", [("fr_carabineer_porte_aigle",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_carabineer_officer", "French Carabineer Uniform", [("fr_carabineer_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_hussards_ranker", "French Hussar Uniform", [("french_hussards_ranker",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_hussards_nco", "French Hussar Uniform", [("french_hussards_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_hussards_officer", "French Hussar Uniform", [("french_hussards_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_hussards_trumpeter", "French Hussar Uniform", [("french_hussards_trumpeter",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_sapper", "Japanese Sapper Kimono", [("gekokujo_hakama_1_5",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_GRaP_body_drummer", "French Drummer Uniform", [("french_GRaP_body_drummer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_GRaP_body_flautist", "French Flautist Uniform", [("french_GRaP_body_flautist",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_voltigeur_body_hornist", "French Voltigeur Uniform", [("french_voltigeur_body_hornist",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_45e_body_drummer", "French Drummer Uniform", [("french_45e_body_drummer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_45e_body_flautist", "French Flautist Uniform", [("french_45e_body_flautist",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_84e_body_drummer", "French Drummer Uniform", [("french_84e_body_drummer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_84e_body_flautist", "French Flautist Uniform", [("french_84e_body_flautist",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["fr_carabineer_trumpeter", "French Trumpeter Uniform", [("fr_carabineer_trumpeter",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["fr_cuirassier_body_trumpeter", "French Trumpeter Uniform", [("fr_cuirassier_body_trumpeter",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_dragoon_body_trumpeter", "French Trumpeter Uniform", [("french_dragoon_body_trumpeter",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_lancer_trumpeter_body", "French Trumpeter Uniform", [("french_lancer_trumpeter_body",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_vistula_body_drummer", "Vistula Legion Uniform", [("french_vistula_body_drummer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_vistula_body_flautist", "Vistula Legion Uniform", [("french_vistula_body_flautist",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_dragoon_body_sargent", "French Dragoon Uniform", [("french_dragoon_body_sargent",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_arty_train", "French Artillery Train Uniform", [("french_arty_train",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_grenadier_a_cheval_body_trumpeter", "French Trumpeter Uniform", [("french_grenadier_a_cheval_body_trumpeter",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["french_captain", "japanese_captain", [("gekokujo_okegawa_short_mori2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["french_equipage_batallion", "Mori tatami", [("gekokujo_tatami_short_8",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],

["french_surgeon", "Surgeon Outfit", [("gekokujo_hakama_2_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],


["nanban1", "Nanban armor", [("gekokujo_nanban_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],

["nanban2", "Nanban armor", [("gekokujo_nanban_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],

["nanban3", "Nanban armor", [("gekokujo_nanban_3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],

["nanban4", "Nanban armor", [("gekokujo_nanban_4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],

["nanban5", "Nanban armor", [("gekokujo_nanban_5",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],

["nanban6", "Nanban armor", [("gekokujo_nanban_6",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],

["nanban7", "Nanban armor", [("gekokujo_nanban_14",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(26)|difficulty(0) ,imodbits_cloth ], 

["jap_armor1", "Japanese Armor", [("gekokujo_bandit_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(5)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
 
["jap_armor2", "Japanese Armor", [("gekokujo_bandit_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(5)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
 
["jap_armor3", "Japanese Armor", [("gekokujo_bandit_3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(5)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],

["jap_armor4", "Japanese Armor", [("gekokujo_bandit_4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(5)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],

["jap_armor5", "Japanese Armor", [("gekokujo_bandit_5",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(5)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
 
["jap_armor6", "Japanese Armor", [("gekokujo_bandit_6",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(5)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
 
["ronin1", "Ronin coat", [("gekokujo_hakama_1_4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["ronin2", "Ronin coat", [("gekokujo_hakama_1_5",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 
["ronin3", "Ronin coat", [("gekokujo_hakama_1_6",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 
["ronin4", "Ronin coat", [("gekokujo_hakama_2_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["ronin5", "Ronin coat", [("gekokujo_hakama_2_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ], 
 
["ronin6", "Ronin coat", [("gekokujo_hakama_2_3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["ronin7", "Ronin coat", [("gekokujo_hakama_2_4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 
["ronin8", "Ronin coat", [("gekokujo_hakama_2_5",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["ronin9", "Ronin coat", [("gekokujo_hakama_2_6",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 
["jap_farmer", "Farmer coat", [("civil_clothing_final",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 
["ninjia1", "Ninja uniform", [("kuijia",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 
["ninjia2", "Ninja uniform", [("renzhebuyi",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 
["jap_mc", "Japanese Mount archer uniform", [("sam_yabusame_cloth",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 
["jap_mc2", "Japanese Mount archer uniform", [("sam_yabusame_cloth2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 
["honda_armor", "Honda armor", [("benduojia",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(8)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 
 #British
["weisuo_uniform", "Weisuo Uniform", [("song_tunic_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_infantry_sarge", "Weisuo Uniform", [("DaMing_wu_jia5",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_infantry_officer", "Weisuo officer armor", [("DaMing_armor_w01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_infantry_drum",  "Ming Qi army uniform", [("song_tunic_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["british_infantry_flute", "Ming Shanwen Ammor", [("mingjia7",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(10)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(28)|difficulty(0) ,imodbits_cloth ],
["british_kgl_ranker", "Ming heavy armor", [("DaMing_armor_01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(7)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
["british_kgl_sarge", "KGL Infantry Uniform", [("british_kgl_sarge",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_kgl_officer", "Ming heavy armor", [("mingjia10",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(7)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
["british_kgl_drum", "KGL Infantry Uniform", [("british_kgl_drum",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_kgl_flute", "KGL Infantry Uniform", [("british_kgl_flute",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_highland_ranker", "Ming spearman armor", [("BL_Song_Byrnie02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(5.5)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
["british_highland_sarge", "Ming spearman armor", [("BL_Song_Byrnie03",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(5.5)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["british_highland_officer", "Qin Liangyu Armor", [("Song_armor_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(7)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
["british_highland_drummer", "British Highland Infantry Uniform", [("british_highland_drummer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_highland_piper", "British Highland Infantry Uniform", [("british_highland_piper",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_highland_piper_2", "British Highland Infantry Uniform", [("british_highland_piper_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_guard_ranker", "British Guard Infantry Uniform", [("british_guard_ranker",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_guard_sarge", "British Guard Infantry Uniform", [("british_guard_sarge",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_guard_officer", "British Guard Infantry Uniform", [("british_guard_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_guard_drum", "British Guard Infantry Uniform", [("british_guard_drum",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_guard_flute", "British Guard Infantry Uniform", [("british_guard_flute",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_light_ranker", "British Light Infantry Uniform", [("british_light_ranker",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_light_sarge", "British Light Infantry Uniform", [("british_light_sarge",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_light_officer", "British Light Infantry Uniform", [("british_light_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_light_bugler", "British Light Infantry Uniform", [("british_light_bugler",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_rifle_ranker", "Ming Musketeer armor", [("mianjia",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["british_rifle_sarge", "British Rifleman Uniform", [("british_rifle_sarge",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_rifle_captain", "Ming Musketeer armor", [("mianjia",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["british_rifle_bugler", "British Rifleman Uniform", [("british_rifle_bugler",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_artillery_ranker", "British Artillery Uniform", [("british_artillery_ranker",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_artillery_officer", "British Artillery Uniform", [("british_artillery_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_artillery_train", "British Artillery Uniform", [("british_artillery_train",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_light_dragoon", "Ming dragoon armor", [("DaMing_armor_09",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["british_light_dragoon_officer", "Ming heavy armor", [("DaMing_armor_1c9",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs |itp_civilian,0,
 100 , weight(8)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
["british_inniskilling_ranker", "Ming mediem armor", [("mingjia4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["british_inniskilling_officer", "Ming Heavy armor", [("mingjia7",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(10)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["british_blue_ranker", "Ming cotton Ammor", [("mingjia2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(4)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(22)|difficulty(0) ,imodbits_cloth ],
["british_blue_officer","Ming cotton Ammor Officer", [("DaMingJiea1yyzp",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(4)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(22)|difficulty(0) ,imodbits_cloth ],
["british_kgl_hussar_ranker", "Ming hussar armor", [("DaMing_armor_10",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_kgl_hussar_officer", "Ming Boader Cavelry Armor",  [("mingjia3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(4)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["british_kgl_hussar_trumpeter", "British Horse Guard Uniform", [("KGL_hussar_trumpeter",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_wellington", "Ming emperor armor", [("DaMing_diwang_armor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(8)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
["british_rocketeer", "British Rocketeer Uniform", [("british_rocketeer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_sapper", "Ming Sapper Uniform", [("bandit_tunic_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(4)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["british_captain", "British Captain Uniform", [("british_captain",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_royal_marine", "British Royal Marine Uniform", [("british_royal_marine",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["naked_female_body", "naked_female_body", [("0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["naked_male_body", "naked_male_body", [("0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["british_surgeon", "Surgeon Outfit", [("Daopao",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["imperial_guard_uniform1", "Imperial Guard Uniform", [("jingyiwei01",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["imperial_guard_uniform2", "mperial Guard Uniform", [("jingyiwei02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["imperial_guard_uniform3", "mperial Guard Uniform", [("jingyiwei03",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["imperial_guard_uniform4", "mperial Guard Uniform", [("jingyiwei04",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
["ming_navy_armor", "Ming Navy armor", [("mingjia_j",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(4)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],

["aoqun1", "Aoqun dress", [("Aoqun",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["aoqun2", "Aoqun dress", [("Aoqun02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["aoqun3", "Aoqun dress", [("Aoqun03",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["aoqun4", "Aoqun dress", [("Aoqun04",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["nvyi1", "Women dress", [("nvyi",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["nvyi2", "Women dress", [("nvyi02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["bijia", "Women dress", [("Bijia",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 
["daao1", "Women dress", [("Daao",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["daao2", "Women dress", [("Daao02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["daao3", "Women dress", [("Daao03",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["korean_skirt", "Korean skirt", [("korean_skirt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],


["western_coat", "Western Coat", [("landsknecht_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(2)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["western_armor", "Western armor", [("german_line_musketeer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(5)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],

["western_armor_off", "Western armor", [("officer_jacket_02",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(4)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
 
 
["princess_robe", "Princess robe", [("Daao03",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],


["moskow_tulup_a", "Tegilai", [("tegilyay1",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
 3960 , weight(6)|abundance(60)|head_armor(0)|body_armor(35)|leg_armor(20)|difficulty(7) ,imodbits_cloth ],
["moskow_tulup_b", "Tegilai", [("tjegilaje_b2",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
 3960 , weight(6)|abundance(60)|head_armor(0)|body_armor(35)|leg_armor(20)|difficulty(7) ,imodbits_cloth ],
["moskow_tulup_c", "Tegilai", [("tjegilaje_b1",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs ,0,
 3960 , weight(6)|abundance(60)|head_armor(0)|body_armor(35)|leg_armor(20)|difficulty(7) ,imodbits_cloth ],

["fysg_bin_shazei01", "fysg_shanzeihu", [("fysg_bin_shazei01", 0),],itp_merchandise|itp_type_body_armor|itp_covers_legs, 0, 
400, weight(10)|abundance(79)|body_armor(20)|leg_armor(12)|difficulty(0), imodbits_cloth ],



 # Prussian
["prussian_infantry_ranker", "swed_leibguard", [("olderinolancerino",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["prussian_infantry_nco", "Prussian Infantry Uniform", [("prussian_8_infantry_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_infantry_officer", "Prussian Infantry Uniform", [("prussian_8_infantry_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_infantry_drum", "Prussian Infantry Uniform", [("prussian_8_infantry_drummer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_infantry_flute", "Prussian Infantry Uniform", [("prussian_8_infantry_fifer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_dragoon_ranker", "Prussian Dragoon Uniform", [("prus_dragoon",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_dragoon_nco", "Prussian Dragoon Uniform", [("prus_dragoon_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_dragoon_officer", "Prussian Dragoon Uniform", [("prus_dragoon_off",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_dragoon_trumpet", "Prussian Dragoon Uniform", [("prus_dragoon_trumpet",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_jaeger_ranker", "Prussian Jaeger Uniform", [("prussian_silesian_ranker",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_jaeger_ranker_alt", "Prussian Jaeger Uniform", [("prussian_silesian_ranker_variant",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_jaeger_nco", "Prussian Jaeger Uniform", [("prussian_silesian_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_jaeger_officer", "Prussian Jaeger Uniform", [("prussian_silesian_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_jaeger_hornist", "Prussian Jaeger Uniform", [("prussian_silesian_hornist",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_guard_ranker", "Prussian Foot Guard Uniform", [("prussian_gzf_ranker",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_guard_nco", "Prussian Foot Guard Uniform", [("prussian_gzf_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_guard_officer", "Prussian Foot Guard Uniform", [("prussian_gzf_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_guard_drummer", "Prussian Foot Guard Uniform", [("prussian_gzf_drummer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_guard_flute", "Prussian Foot Guard Uniform", [("prussian_gzf_fifer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_arty_ranker", "Prussian Artillery Uniform", [("prussian_artillery_ranker",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_arty_train", "Prussian Artillery Uniform", [("prussian_artillery_train",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_arty_officer", "Prussian Artillery Uniform", [("prussian_artillery_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_hussar_ranker", "Prussian Hussar Uniform", [("copy_copy_mongol_hal",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_hussar_nco", "Prussian Hussar Uniform", [("prussian_hussar_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_hussar_officer", "Prussian Hussar Uniform", [("prussian_hussar_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_hussar_officer_variant", "Prussian Hussar Uniform", [("prussian_hussar_officer_variant",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_hussar_trumpet", "Prussian Hussar Uniform", [("prussian_hussar_trumpeter",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_infantry2_ranker", "Prussian Infantry Uniform", [("ruperthorseofficer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
["prussian_infantry2_nco", "Prussian Infantry Uniform", [("prussian_23_infantry_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_infantry2_officer", "Prussian Infantry Uniform", [("prussian_23_infantry_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_infantry2_drum", "Spanish Infantry Uniform", [("talbotdrum",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_infantry2_flute", "Prussian Infantry Uniform", [("prussian_23_infantry_fifer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_landwehr_ranker", "Prussian Landwehr Uniform", [("prussian_landwehr_ranker",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_landwehr_ranker_alt", "Prussian Landwehr Uniform", [("prussian_landwehr_ranker_variant",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_landwehr_nco", "Prussian Landwehr Uniform", [("prussian_landwehr_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_landwehr_officer", "Prussian Landwehr Uniform", [("prussian_landwehr_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_landwehr_drum", "Prussian Landwehr Uniform", [("prussian_landwehr_drummer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_landwehr_flute", "Prussian Landwehr Uniform", [("prussian_landwehr_fifer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_landwehr_cav_ranker", "Prussian Landwehr Uniform", [("prussian_landwehr_cavalry_ranker",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_landwehr_cav_nco", "Prussian Landwehr Uniform", [("prussian_landwehr_cavalry_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_landwehr_cav_officer", "Prussian Landwehr Uniform", [("prussian_landwehr_cavalry_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_landwehr_cav_trumpet", "Prussian Landwehr Uniform", [("prussian_landwehr_cavalry_trumpeter",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_blucher", "Blucher's Uniform", [("blucher",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_cuirassier_ranker", "Prussian Cuirassier Uniform", [("prussian_cuirassier_ranker",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,  #patch1115 25/3 begin
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_cuirassier_nco", "Prussian Cuirassier Uniform", [("prussian_cuirassier_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_cuirassier_officer", "Prussian Cuirassier Uniform", [("prussian_cuirassier_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_cuirassier_trumpet", "Prussian Cuirassier Uniform", [("prussian_cuirassier_trumpeter",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ], #patch1115 25/3 end
["prussian_freikorps_ranker", "Prussian Freikorps Uniform", [("prussian_lutzov_ranker",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_freikorps_nco", "Prussian Freikorps Uniform", [("prussian_lutzov_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_freikorps_officer", "Prussian Freikorps Uniform", [("prussian_lutzov_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_freikorps_drum", "Prussian Freikorps Uniform", [("prussian_lutzov_drummer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_freikorps_flute", "Prussian Freikorps Uniform", [("prussian_lutzov_fifer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_pioneer", "Prussian Pioneer Uniform", [("prussian_pioneer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["prussian_surgeon", "Surgeon Outfit", [("surgeon_coat",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["coat1", "Spanish recuit suit", [("norfolk_pikeman1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["coat2", "Spanish recuit suit", [("norfolk_pikeman2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 
["coat3", "Spanish recuit suit", [("norfolk_pikeman3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["coat4", "Spanish recuit suit", [("norfolk_pikeman4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["coat5", "Spanish recuit suit", [("norfolk_pikeman5",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 
["coat6", "Spanish recuit suit", [("puritan_priest",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 
["pikeman_armor1", "Pikeman armor", [("merc_pikeman_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],

["pikeman_armor2", "Pikeman armor", [("merc_pikeman_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
 
["dragoon_armor", "Pikeman armor", [("merc_pikeman_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(7)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(24)|difficulty(0) ,imodbits_cloth ],
 
["firelockman_armor1", "firelockman armor", [("trumpeter_fairfax",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(4)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
 
["firelockman_armor2", "firelockman armor", [("breastplate_on_plain",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(4)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
 
["firelockman_armor3", "firelockman armor", [("breastplate_on_red",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(4)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
 
["firelockman_armor4", "firelockman armor", [("16th_jiaohuangdui",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(5)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
 
["royal_guards_armor", "Royal Guards armor", [("zhongjia_5",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(8)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 
["norfolk_pikeman5", "hussar armor", [("norfolk_pikeman5",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
 
["s1wed_pikeman", "hussar armor", [("16th_merc_pikeman_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(18)|difficulty(0) ,imodbits_cloth ],
 
["gothic_armor_holy_rome", "heavy armor", [("gothic_armor_Holy_Rome",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(9)|abundance(100)|head_armor(0)|body_armor(65)|leg_armor(40)|difficulty(0) ,imodbits_cloth ],
 
["henjiahenjbanb", "heavy officer armor", [("bnw_armour_hr",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(25)|difficulty(0) ,imodbits_cloth ],
 
["merc_pikeman_a", "heavy armor", [("merc_pikeman_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(4)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
 
["jaguar_armour4", "heavy armor", [("jaguar_armour4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(2)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
 
["jaguar_armour", "heavy armor", [("jaguar_armour",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(2)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
 
["roman_light_armor_red", "Inca bronze armour", [("roman_light_armor_red",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],#yin jia
 
["drz_kaftan2", "spanish armada", [("drz_kaftan2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],#wu di jian dui
 
["gambeson_engxb", "spanish armada officer", [("gambeson_engxb",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],#wu di jian dui zhi hui guan
 
["t_helmet_b_a", "fei li si shi kai jia", [("t_helmet_b_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],#wu di jian dui zhi hui guan
 # Russian
["russian_infantry1", "Russian Infantry Uniform", [("qingjia1_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(6)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["russian_infantry_nco", "Russian Infantry Uniform", [("qingjia1_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_infantry_officer", "Russian Infantry Uniform", [("rus_musketeer_off",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_drummer", "Russian Infantry Uniform", [("rus_drummer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_flautist", "Russian Infantry Uniform", [("rus_flautist",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_hussar_officer", "Mongo Uniform", [("mongol_hal",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3.5)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["russian_hussar_nco", "Russian Hussar Uniform", [("rus_hussards_sarg",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_hussar_ranker", "Russian Hussar Uniform", [("copy_copy_mongol_hal",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_hussar_trumpeter", "Russian Hussar Uniform", [("rus_hussards_trump",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_horse_guard", "Yellow Flag Armor", [("qingjia1_7",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
["russian_horse_guard_nco", "Russian Chevalier-Garde Uniform", [("rus_chevalier_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_horse_guard_officer", "Russian Chevalier-Garde Uniform", [("rus_chevalier_off",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_horse_guard_trumpeter", "Russian Chevalier-Garde Uniform", [("rus_chevalier_trump",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_cossack_officer", "Blue flag cavlary", [("qingjia1_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(7)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
["russian_cossack", "White Flag Cavlary", [("qingjia1_6",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(7)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
["Kutuzov", "Kutuzov Uniform", [("qingjia_htj",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(7)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
["russian_militia_officer", "Russian Militia Officer Uniform", [("rus_militia_off",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_militia_ranker", "Russian Militia Uniform", [("rus_militia_ranker",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_guard_officer", "Russian Guard Infantry Uniform", [("rus_preobr_off",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_guard_nco", "Russian Guard Infantry Uniform", [("rus_preobr_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_guard_ranker", "Qing Red armor", [("qingjia1_3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(7)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
["russian_guard_drummer", "Russian Guard Infantry Uniform", [("rus_preobr_drummer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_guard_flautist", "Russian Guard Infantry Uniform", [("rus_flautist_preobr",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_jaeger_officer", "Qing Red armor", [("qingjia1_4",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(7)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
["russian_jaeger_nco", "Russian Jaeger Uniform", [("rus_jaeger_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_jaeger_ranker", "Russian Jaeger Uniform", [("rus_jaeger",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_jaeger_musician", "Russian Jaeger Uniform", [("rus_jaeger_drum",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_gren_officer", "Russian Infantry Uniform", [("rus_pavlo_off",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_gren_nco", "Russian Infantry Uniform", [("rus_pavlo_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_gren_ranker", "Russian Infantry Uniform", [("rus_pavlo_ranker",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_arty_officer", "Russian Artillery Uniform", [("rus_arty_off",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_arty_nco", "Russian Artillery Uniform", [("rus_arty_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_arty_ranker", "Russian Artillery Uniform", [("rus_arty_ranker",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_dragoon_officer", "Russian Dragoon Uniform", [("rus_dragoon_off",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_dragoon_nco", "Russian Dragoon Uniform", [("rus_dragoon_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_dragoon_ranker", "qing_firemancloth", [("qing_firemancloth",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_dragoon_trumpeter", "Russian Dragoon Uniform", [("rus_dragoon_trump",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["rus_partizan1", "Russian Great Coat", [("qingbin2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["rus_partizan2", "Russian Great Coat", [("qingbin",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_uhlan_officer", "Yellow Flag Officer Armor", [("qingjia1_8",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(7)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
["russian_uhlan_nco", "Russian Uhlan Uniform", [("rus_uhlan_NCO",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_uhlan_ranker", "Yellow Flag Armor", [("qingjia1_8",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(7)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
["russian_uhlan_trumpeter", "Russian Uhlan Uniform", [("rus_uhlan_trumpeter",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["rus_pioneer", "Russian Pioneer Uniform", [("rus_pioneer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["russian_surgeon", "Surgeon Outfit", [("russia_surgeon",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["tatar_coat", "Tatar Coat", [("tatar_coat2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["qing_coat1", "Qing Coat", [("luying_bing",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

["khergit_lady_dress", "Khergit Lady Dress", [("khergit_lady_dress",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 
500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
 
["qing_dress1", "Qing Dress", [("qing_nvzhuang1",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 
500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
  
["qing_dress2", "Qing Dress", [("qing_nvzhuang3",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 
500 , weight(3)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
# Austrian
["austrian_infantry", "Austrian Infantry Uniform", [("austrian_infantry",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_infantry_nco", "Austrian Infantry Uniform", [("austrian_infantry_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_infantry_officer", "Austrian Infantry Uniform", [("austrian_infantry_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_infantry_drummer", "Austrian Infantry Uniform", [("austrian_infantry_drummer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_infantry_fifer", "Austrian Infantry Uniform", [("austrian_infantry_musician",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_infantry2", "Hungarian Infantry Uniform", [("austrian_infantry2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_infantry2_nco", "Hungarian Infantry Uniform", [("austrian_infantry2_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_infantry2_officer", "Hungarian Infantry Uniform", [("austrian_infantry2_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_infantry2_drummer", "Hungarian Infantry Uniform", [("austrian_infantry2_drummer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_infantry2_fifer", "Hungarian Infantry Uniform", [("austrian_infantry2_musician",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_grenadier", "Hungarian Infantry Uniform", [("austrian_grenadier",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_grenadier_alt", "Hungarian Infantry Uniform", [("austrian_grenadier_var1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_grenadier_nco", "Hungarian Infantry Uniform", [("austrian_grenadier_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_grenadier_officer", "Hungarian Infantry Uniform", [("austrian_grenadier_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_grenadier_drummer", "Hungarian Infantry Uniform", [("austrian_grenadier_drummer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_grenadier_fifer", "Hungarian Infantry Uniform", [("austrian_grenadier_musician",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_grenzer", "Austrian Grenzer Uniform", [("austrian_grenzer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_grenzer_nco", "Austrian Grenzer Uniform", [("austrian_grenzer_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_grenzer_officer", "Austrian Grenzer Uniform", [("austrian_grenzer_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_grenzer_drummer", "Austrian Grenzer Uniform", [("austrian_grenzer_drummer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_grenzer_fifer", "Austrian Grenzer Uniform", [("austrian_grenzer_musician",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_jaeger", "Austrian Jaeger Uniform", [("austrian_jaeger",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_jaeger_nco", "Austrian Jaeger Uniform", [("austrian_jaeger_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_jaeger_officer", "Austrian Jaeger Uniform", [("austrian_jaeger_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_jaeger_hornist", "Austrian Jaeger Uniform", [("austrian_jaeger_hornist",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_lightcav", "Austrian Chevau-leger Uniform", [("austrian_lightcav",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_lightcav_nco", "Austrian Chevau-leger Uniform", [("austrian_lightcav_flag_bearer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_lightcav_trumpet", "Austrian Chevau-leger Uniform", [("austrian_lightcav_trumpeter",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_lightcav_officer", "Austrian Chevau-leger Uniform", [("austrian_lightcav_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_dragoon", "Austrian Dragoon Uniform", [("austrian_dragoon",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_dragoon_nco", "Austrian Dragoon Uniform", [("austrian_dragoon_flag_bearer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_dragoon_trumpet", "Austrian Dragoon Uniform", [("austrian_dragoon_trumpeter",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_dragoon_officer", "Austrian Dragoon Uniform", [("austrian_dragoon_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_uhlan", "Austrian Uhlan Uniform", [("austrian_uhlan",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_uhlan_nco", "Austrian Uhlan Uniform", [("austrian_uhlan_flag_bearer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_uhlan_trumpet", "Austrian Uhlan Uniform", [("austrian_uhlan_trumpeter",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_uhlan_officer", "Austrian Uhlan Uniform", [("austrian_uhlan_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_arty", "Austrian Artillery Uniform", [("austrian_arty",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_arty_train", "Austrian Artillery Uniform", [("austrian_arty_train",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_arty_officer", "Austrian Artillery Uniform", [("austrian_arty_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_pioneer", "Austrian Pioneer Uniform", [("austrian_pioneer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_hussar", "Austrian Hussar Uniform", [("austrian_hussar",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_hussar_nco", "Austrian Hussar Uniform", [("austrian_hussar_flag_bearer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_hussar_trumpet", "Austrian Hussar Uniform", [("austrian_hussar_trumpeter",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_hussar_officer", "Austrian Hussar Uniform", [("austrian_hussar_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_cuiraisser", "Austrian Cuirassier Uniform", [("austrian_cuirassier_ranker",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_cuiraisser_nco", "Austrian Cuirassier Uniform", [("austrian_cuirassier_flag_bearer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_cuiraisser_trumpet", "Austrian Cuirassier Uniform", [("austrian_cuirassier_trumpeter",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_cuiraisser_officer", "Austrian Cuirassier Uniform", [("austrian_cuirassier_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_schwarzenberg", "Schwarzenberg's Uniform", [("schwarzenberg",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["austrian_surgeon", "Surgeon Outfit", [("austria_surgeon",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 
 
["russian_militia_uniform", "Russian militia uniform", [("empire_gambeson_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 
["russian_pike_man_armor", "Russian pike man armor", [("moskow_reytar",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
 
["russian_pike_man_officer_armor", "Russian pike man officer armor", [("moskow_reytar",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
 
["russian_firelock_man_armor", "Russian firelock man armor", [("mosk_streletz_pure",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.8)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
 
["russian_firelock_man_officer_armor", "Russian firelock man officer armor", [("ukr_jupan_siniy",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.8)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
 
["stelz_armor", "Stelz armor", [("old_tjegilaje_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.8)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],

["stelz_armor_off", "Stelz armor", [("tjegilaje_a2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.8)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],

["tsar_pro_military_uniform", "Tsar pro-military uniform", [("strelets_a2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.8)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
 
["tsar_pro_military_uniform_officer", "Tsar pro-military uniform officer", [("muscov_officer_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.8)|abundance(100)|head_armor(0)|body_armor(32)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
 
["uniform_of_russian_hussars", "Uniform of Russian hussars", [("uniform_of_russian_hussars",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.8)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
 
["uniform_of_russian_hussars_officer", "Uniform of Russian hussars officer", [("poland_dragoon",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.8)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
 
["raether_pistol_cavalry_armor", "Raether pistol cavalry armor", [("moskow_reytar",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.8)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
 
["raether_pistol_cavalry_officer_armor", "Raether pistol cavalry officer armor", [("reytar_puzo",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.8)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(25)|difficulty(0) ,imodbits_cloth ],
 
["cossack_cavalry_uniform", "Cossack cavalry uniform", [("ua_shirt_a2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.8)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],

["cossack_cavalry_uniform2", "Cossack cavalry uniform", [("ua_shirt_c3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.8)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],

["cossack_cavalry_uniform3", "Cossack cavalry uniform", [("ua_shirt_a1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.8)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],

["cossack_cavalry_uniform4", "Cossack cavalry uniform", [("ua_shirt_a0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.8)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],

["cossack_cavalry_uniform_officer", "Cossack cavalry uniform officer", [("ua_skin_vest_a1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.8)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
 
["boyar_noble_cavalry_uniform", "Boyar noble cavalry uniform", [("mosk_bahter_simple",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(2.0)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(25)|difficulty(0) ,imodbits_cloth ],
 
["boyar_noble_cavalry_uniform_officer", "Boyar noble cavalry uniform officer", [("mosk_kuyak",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(2.0)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(28)|difficulty(0) ,imodbits_cloth ],
 
["opry_armor", "opry armor", [("mosk_kuyak",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(2.0)|abundance(100)|head_armor(0)|body_armor(50)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 
["russian_doctor_clothing", "Russian doctor clothing", [("cvl_costume_a2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(2.0)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
 
["russian_engineering_suit", "Russian engineering suit", [("wei_xiadi_kher_kaftan",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(2.0)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
 
["romanov_armor", "Romanov armor", [("mosk_zertzalo",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(2.0)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],


# Rhine
["bavarian_inf_ranker", "Bavarian Uniform", [("bavarian_inf_ranker",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["bavarian_inf_flagcarrier", "Bavarian Uniform", [("bavarian_inf_flagcarrier",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["bavarian_inf_officer", "Bavarian Uniform", [("bavarian_inf_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["bavarian_inf_drummer", "Bavarian Uniform", [("bavarian_inf_drummer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["bavarian_inf_flutist", "Bavarian Uniform", [("bavarian_inf_flutist",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["bavarian_jaeger_ranker", "Bavarian Uniform", [("bavarian_jaeger_body_ranker",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["bavarian_jaeger_nco", "Bavarian Uniform", [("bavarian_jaeger_body_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["bavarian_jaeger_officer", "Bavarian Uniform", [("bavarian_jaeger_body_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["bavarian_jaeger_hornist", "Bavarian Uniform", [("bavarian_jaeger_body_hornist",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["bavarian_artillery_ranker", "Bavarian Uniform", [("bavarian_artillery_body_ranker",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["bavarian_artillery_train", "Bavarian Uniform", [("bavarian_artillery_train_body",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["bavarian_artillery_officer", "Bavarian Uniform", [("bavarian_artillery_officer_body",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["saxon_inf_ranker", "Saxon Uniform", [("saxon_infantry_body_ranker",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["saxon_inf_nco", "Saxon Uniform", [("saxon_infantry_body_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["saxon_inf_officer", "Saxon Uniform", [("saxon_infantry_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["saxon_inf_drummer", "Saxon Uniform", [("saxon_infantry_drummer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["saxon_inf_fifer", "Saxon Uniform", [("saxon_inf_flutist",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["saxon_uhlan_ranker", "Saxon Uniform", [("saxon_ulan_private",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["saxon_uhlan_ranker_alt", "Saxon Uniform", [("saxon_ulan_private_2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["saxon_uhlan_nco", "Saxon Uniform", [("saxon_ulan_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["saxon_uhlan_officer", "Saxon Uniform", [("saxon_ulan_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["saxon_uhlan_trumpet", "Saxon Uniform", [("saxon_ulan_trumpeter",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["hessian_inf_ranker", "Hessian Uniform", [("hessen_infantry_private",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["hessian_inf_nco", "Hessian Uniform", [("hessen_infantry_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["hessian_inf_officer", "Hessian Uniform", [("hessen_infantry_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["rhine_surgeon", "Surgeon Outfit", [("rhine_surgeon",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["westphalian_guard_ranker", "Westphalian Uniform", [("west_gr_ranker",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["westphalian_guard_nco", "Westphalian Uniform", [("west_gr_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["westphalian_guard_officer", "Westphalian Uniform", [("west_gr_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["westphalian_guard_drummer", "Westphalian Uniform", [("west_gr_drummer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["westphalian_guard_fifer", "Westphalian Uniform", [("west_gr_fifer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["saxon_king", "Royal Outfit", [("saxonyking",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["nassau_jaeger_ranker", "Nassauer Uniform", [("nassau_ranker",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["nassau_jaeger_nco", "Nassauer Uniform", [("nassau_nco",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["nassau_jaeger_officer", "Nassauer Uniform", [("nassau_off",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["nassau_jaeger_trumpet", "Nassauer Uniform", [("nassau_trumpeter",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["wurttemberg_inf_ranker", "wurttemberg Uniform", [("wurttemberg_private",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["wurttemberg_inf_flagcarrier", "wurttemberg Uniform", [("wurttemberg_NCO",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["wurttemberg_inf_officer", "wurttemberg Uniform", [("wurttemberg_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["wurttemberg_inf_drummer", "wurttemberg Uniform", [("wurttemberg_drummer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["wurttemberg_inf_flutist", "wurttemberg Uniform", [("wurttemberg_fifer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["wurttemberg2_inf_ranker", "wurttemberg2 Uniform", [("wurttemberg_grenadier_private",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["wurttemberg2_inf_flagcarrier", "wurttemberg2 Uniform", [("wurttemberg_grenadier_NCO",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["wurttemberg2_inf_officer", "wurttemberg2 Uniform", [("wurttemberg_grandier_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["wurttemberg2_inf_drummer", "wurttemberg2 Uniform", [("wurttemberg_grenadier_drummer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["wurttemberg2_inf_flutist", "wurttemberg2 Uniform", [("wurttemberg_grenadier_fifer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["berg_pioneer", "berg_pioneer Uniform", [("berg_pioneer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["saxon_garde_ranker", "Saxon Cuirassier Uniform", [("garde_du_corps",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["saxon_garde_colours", "Saxon Cuirassier Uniform", [("garde_du_corps_NCO",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["saxon_garde_officer", "Saxon Cuirassier Uniform", [("garde_du_corps_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["saxon_garde_body_trumpeter", "Saxon Trumpeter Uniform", [("garde_du_corps_trumpeter",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["westphalian_cuirassier_ranker", "Westphalian Cuirassier Uniform", [("westphalian_cuirassier_body_ranker",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["westphalian_cuirassier_colours", "Westphalian Cuirassier Uniform", [("westphalian_cuirassier_NCO",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["westphalian_cuirassier_officer", "Westphalian Cuirassier Uniform", [("westphalian_cuirassier_body_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["westphalian_cuirassier_body_trumpeter", "Westphalian Trumpeter Uniform", [("westphalian_cuirassier_trumpeter",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["baden_dragoon_ranker", "Austrian Chevau-leger Uniform", [("baden_dragoon_private",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["baden_dragoon_nco", "Austrian Chevau-leger Uniform", [("baden_dragoon_NCO",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["baden_dragoon_trumpet", "Austrian Chevau-leger Uniform", [("baden_dragoon_trumpeter",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["baden_dragoon_officer", "Austrian Chevau-leger Uniform", [("baden_dragoon_officer",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 
 
["kabukuru_clothing1", "kabukuru_clothing1", [("Pol_svitka_pure_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 
["kabukuru_clothing2", "kabukuru_clothing2", [("Pol_svitka_pure_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 
["kabukuru_clothing3", "kabukuru_clothing3", [("Pol_svitka_pure_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 
["kabukuru_clothing4", "kabukuru_clothing4", [("Pol_svitka_pure_d",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 
["coral_armor", "Coral armor", [("omsipahi_zirhi_1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
 
["coral_armor_officer", "Coral armor officer", [("goldsipahi",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
 
["huoqiangshou_clothes", "Huoqiangshou clothes", [("turk_azap",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.2)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],

["ottoman_officer_robe", "Ottoman officer robe", [("arab_bandit_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.2)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
 
["sudan_qinbing_uniform", "Sudan qinbing uniform1", [("janichar2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.2)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
 
["sudan_qinbing_uniform2", "Sudan qinbing uniform2", [("janichar1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.2)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
 
["sudan_qinbing_uniform_officer", "Sudan qinbing uniform officer", [("janichareteksiz",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.2)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
 
["holy_warrior_armor", "Holy Warrior Armor", [("Pol_svitka_pure_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.2)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
 
["turkmen_robe", "Turkmen robe", [("saracenmails",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.2)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
 
["mamluk_armor", "Mamluk armor", [("sarranid_elite_cavalary",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(48)|leg_armor(25)|difficulty(0) ,imodbits_cloth ],
 
["pirate_clothes", "Pirate clothes", [("delilarmor",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
 
["deni_apza_navy", "Deni Apza Navy", [("janichareteksiz_23",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
 
["deni_apza_navy_officer", "Deni Apza Navy", [("turkish_coat_c5",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
 
["guards_artillery_clothes", "Guards artillery clothes", [("blue_gambeson_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
 
["engineer_suit", "Engineer suit", [("arena_tunicR_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
 
["doctor_suit", "doctor suit", [("arena_tunicW_new",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
 
["muhammad_robe", "Muhammad robe", [("rinda",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
 
["jerusalem_camel_warrior_armor", "Jerusalem camel warrior armor", [("sarazinass",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.4)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
 
 
#Civilian Shirts
["civil_shirt_1", "Civilian Shirt 1", [("civil_shirt_1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 100, weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["civil_shirt_2", "Civilian Shirt 1", [("civil_shirt_2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 100, weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],

 # Character screen uniform
["character_uniform", "{!}Character Uniform Dummy", [("character_uniform",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 
#Poland
#波兰
 ["poland_uniform", "Bavarian Uniform", [("rp_justacorps_a0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 ["blyqbj1", "blyqbj1", [("pol_krilatiy_gusar_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 ["blyqbj2", "blyqbj2", [("pol_husar_yaguar",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 ["blyqbj3", "blyqbj3", [("pol_krilatiy_gusar",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 ["blyqbj4", "blyqbj4", [("pol_krilatiy_gusar_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 ["blszj1", "blszj1", [("pancer_red1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["blszj2", "blszj2", [("pancer_blue1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["blszj3", "blszj3", [("pancer_green1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(24)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["blszj4", "blszj4", [("pancer_red3.0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
 ["blszjz1", "blszjz1", [("pancer_blue3.0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 ["blszjz2", "blszjz2", [("pancer_green3.0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 ["blszjz3", "blszjz3", [("pancer_red4.0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 ["blszjz4", "blszjz4", [("pancer_ch1.0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 ["blszjz5", "blszjz5", [("pancer_blue4.0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 ["blszjz6", "blszjz6", [("pancer_green4.0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(2.5)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(9)|difficulty(0) ,imodbits_cloth ],
 ["blszjq1", "blszjq1", [("pancer_orn_a1.0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(3)|difficulty(0) ,imodbits_cloth ],
 ["blszjcz1", "blszjcz1", [("pancer_orn_b4.0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(3)|difficulty(0) ,imodbits_cloth ],
 ["blszjqq1", "blszjqq1", [("pancer_orn_b1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(2)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(3)|difficulty(0) ,imodbits_cloth ],
 ["blszjqq2", "blszjqq2", [("pancer_orn_a3.0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(2)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(3)|difficulty(0) ,imodbits_cloth ],
 ["blszjqq3", "blszjqq3", [("pancer_orn_b3.0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(2)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(3)|difficulty(0) ,imodbits_cloth ],
 ["blszjqqz1", "blszjqz1", [("pancer_orn_a4.0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(3)|abundance(100)|head_armor(0)|body_armor(30)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
 ["blszjqq4", "blszjqq4", [("pancer_ch2.0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(2)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(3)|difficulty(0) ,imodbits_cloth ],
 ["blnmyfd1", "blnmyf1", [("rp_wams_ch1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(3)|difficulty(0) ,imodbits_cloth ],
 ["blnmyfc1", "blnmyfc1", [("lt_justacorps_a1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
 ["blnmyfc2", "blnmyfc2", [("lt_justacorps_a2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
 ["blnmyfc3", "blnmyfc3", [("lt_justacorps_ch1.0.0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
 ["blnmyfc4", "blnmyfc4", [("lt_justacorps_o1.0.0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
 ["blmb1", "blmb1", [("rp_justacorps_a0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
 ["blmb2", "blmb2", [("rp_justacorps_a1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
 ["blmb3", "blmb3", [("rp_justacorps_a2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
 ["blmb4", "blmb4", [("rp_justacorps_b1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
 ["blmb5", "blmb5", [("rp_justacorps_b2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
 ["blmb6", "blmb6", [("rp_justacorps_ch2.0.0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
 ["blmb7", "blmb7", [("rp_justacorps_o2.0.0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
 ["gskyf1", "gskyf1", [("rp_zupan_a0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
 ["gskyf2", "gskyf2", [("rp_zupan_a1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
 ["gskyf3", "gskyf3", [("rp_zupan_a2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
 ["gskyf4", "gskyf4", [("rp_zupan_a3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
 ["gskyf5", "gskyf5", [("rp_zupan_ch1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
 ["gskyf6", "gskyf6", [("rp_zupan_o1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
 ["gskyfz8", "gskyfz8", [("rp_zupan_o2.1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
 ["gskyfc1", "gskyfc1", [("rp_delia_a1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["gskyfc2", "gskyfc2", [("rp_delia_a2",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["gskyfc3", "gskyfc3", [("rp_delia_ch1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["gskyfc4", "gskyfc4", [("rp_delia_o1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["blyfc1", "blyfc1", [("old_wal_coast_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["blyfc2", "blyfc2", [("wal_coast_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["blyfc3", "blyfc3", [("wal_coast_b",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["blyfc4", "blyfc4", [("wal_coast_c",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["blyfc5", "blyfc5", [("wal_coast_c1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["blyfc6", "blyfc6", [("wal_coast_c2.0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["blyfc7", "blyfc7", [("wal_coast_c3",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["blyfc8", "blyfc8", [("wal_coast_c4.0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["blyfc9", "blyfc9", [("zupan_gray_a1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["blyfc10", "blyfc10", [("zupan_red_a1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["blyfc11", "blyfc11", [("zupan_blue_a1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["blyfc12", "blyfc12", [("zupan_green_a1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["blyfc13", "blyfc13", [("zupan_orn_red_a1",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["blqbj1", "blqbj1", [("old_huss_anima.0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
 ["blqbj2", "blqbj2", [("red_huss_anima.0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
 ["blqbj3", "blqbj3", [("red_huss_anima_chain.0",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 100 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
#头盔
#Hats
["rus_pavlovsk_ranker", "Pavlovsk Ranker Mitras Cap", [("rus_pavlovsk_ranker",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_kyiv_dragoons_all", "Russian Dragoon Helmet", [("nuanmao_pu",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_kyiv_dragoons_trumpeter", "Russian Dragoon Trumpeter Helmet", [("luyingmao1_xp",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_drummer_shako", "Bule Flag Infantry Helmet", [("shicong",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_chevalier_hat", "Yellow Flag Helmet", [("rus_chevalier_hat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_chevalier_hat_officer", "Yellow Flag Helmet", [("daqingzhou1_7",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_chevalier_hat_trumpeter", "Russian Chevalier-Garde Helmet", [("rus_chevalier_hat_trump",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_arty_shako_officer", "Russian Artillery Shako", [("rus_arty_captain_shako",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_arty_shako_nco", "Russian Artillery Shako", [("rus_arty_sarge_shako",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_arty_shako_ranker", "Russian Artillery Shako", [("daqingzhou1_2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_cossack_hat_officer", "White flag helmet Officer", [("daqingzhou1_6",0)], itp_merchandise| itp_type_head_armor |itp_civilian |itp_doesnt_cover_hair ,0, 4 , weight(2.0)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_cossack_hat_nco", "Blue flag Helmet", [("shicong1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_cossack_hat_ranker", "White flag helmet", [("shicong5",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_hussar_shako_officer", "Russian Hussar Shako", [("mon_hat_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_hussar_shako_nco", "Russian Hussar Shako", [("rus_hussard_sarge_shako",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_hussar_shako_ranker", "Russian Hussar Shako", [("1mon_hat_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_hussar_shako_trumpeter", "Russian Hussar Shako", [("rus_hussard_trumpeter_shako",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_jaeger_shako_nco", "Russian Jaeger Shako", [("shicong6",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_jaeger_shako_ranker", "Russian Jaeger Shako", [("daqingzhou1_8",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["kutuzov_hat", "Kutuzov Hat", [("qingkui_htj",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_covers_beard  ,0, 4 , weight(1.5)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_guard_shako_officer", "Russian Guard Infantry Shako", [("daqingzhou1_3",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_guard_shako_nco", "Russian Guard Infantry Shako", [("rus_preobr_sarge_shako",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_guard_shako_ranker", "Qing helmet", [("shicong2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_guard_shako_musician", "Blue Flag Officer Helmet", [("daqingzhou1_1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_infantry_officer_shako", "Qing helmet", [("jiangkui_b",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_infantry_shako_nco", "Russian Infantry Shako", [("rus_musketeer_sarge_shako",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_pioneer_shako", "Russian Pioneer Shako", [("shako_rus_pioneer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_partisan_hat1", "Peasant's Cap", [("rus_random_hat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_partisan_hat2", "Peasant's Cap", [("rus_random_hat1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_partisan_hat3", "Peasant's Cap", [("partizan_hat_1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_partisan_hat4", "Peasant's Cap", [("partizan_hat_2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_partisan_hat5", "Peasant's Cap", [("partizan_hat_3",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_uhlan_czapka_officer", "Russian Uhlan Czapka", [("czapka_officer_uhlan",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair|itp_attach_armature  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_uhlan_czapka_nco", "Russian Uhlan Czapka", [("czapka_nco_uhlan",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair|itp_attach_armature  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_uhlan_czapka_ranker", "Russian Uhlan Czapka", [("czapka_ranker_uhlan",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair|itp_attach_armature  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_uhlan_czapka_trumpeter", "Russian Uhlan Czapka", [("czapka_trump_uhlan",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair|itp_attach_armature  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

  #French
["french_dragoon_helmet", "Japanese Head warp", [("sugo_cap_white",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["french_dragoon_helmet_officer", "Dane helmet", [("gekokujo_zunari_o_h_1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["french_dragoon_helmet_trumpeter", "Dragoon Helmet", [("french_dragons_dlG_trumpeter",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["french_cuirassier_helmet", "Takeda Helmet", [("gekokujo_kabuto3_h_3",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["french_cuirassier_helmet_officer", "Takeda Helmet", [("gekokujo_kabuto2_r_3",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair ,0, 4 , weight(1.5)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["french_cuirassier_helmet_trumpeter", "Cuirassier Helmet", [("french_cuirassier_helmet_trumpeter",0)], itp_merchandise| itp_type_head_armor |itp_civilian ,0, 4 , weight(1.5)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["french_carabineer_helmet", "Carbinier Helmet", [("french_carabineer_ranker",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["french_carabineer_helmet_officer", "Carbinier Helmet", [("french_carabineer_officer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["french_carabineer_helmet_trumpeter", "Carbinier Helmet", [("french_carabineer_trumpeter",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["french_hussar_shako_colours", "Hussar Shako", [("french_hussar_shako_colours",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["french_hussar_shako_ranker", "Hussar Shako", [("french_hussar_shako_ranker",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["french_hussar_shako_trumpeter", "Hussar Shako", [("french_hussar_shako_trumpeter",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["french_inf_shako_45_ranker", "Infantry Shako", [("french_inf_shako_45_ranker",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["french_vistula_shako_colours", "Infantry Shako", [("french_vistula_shako_colours",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["french_vistula_shako_ranker", "Samurai Helmet", [("zunari_newred",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["samurai_helmet", "Samurai Helmet", [("gekokujo_new_shic_3",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["french_vistula_shako_officer", "Samurai Helmet", [("gekokujo_kabuto2_h_3",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["french_inf_shako_84_colours", "Infantry Shako", [("french_inf_shako_84_colours",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["french_inf_shako_84_ranker", "Infantry Shako", [("gekokujo_jingasa_1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["french_inf_shako_84_officer", "Infantry Shako", [("gekokujo_jingasa_1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],  
["french_voltigeur_shako_officer", "Japanese helmet", [("gekokujo_suji_o_2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["french_voltigeur_shako_ranker", "Japanese infantry hat", [("gekokujo_jingasa_chosokabe",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["french_ldlg_czapka_officer", "Guard Lancer Czapka", [("french_LdlG_officer_czapka",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["french_ldlg_czapka_ranker", "Guard Lancer Czapka", [("french_LdlG_ranker_czapka",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["french_ldlg_czapka_trumpeter", "Guard Lancer Czapka", [("french_LdlG_trumpeter_czapka",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["french_artillery_bearskin_officer", "Artillery Bearskin", [("french_artillery_captain_bearskin",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["french_artillery_bearskin_ranker", "Otomo hat", [("gekokujo_jingasa_otomo",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["french_gap_bearskin_officer", "Suji", [("spk",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(32)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["french_gap_bearskin_colours", "Grenadiers a Pied Bearskin", [("french_GaP_flagcarrier_bearskin",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["french_gap_bearskin_ranker", "Suji", [("gekokujo_suji_o_1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["french_sapper_bearskin", "Sugo", [("sugo_cap_white",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["french_inf_bicorne_45_officer", "Infantry Bicorne", [("french_inf_bicorne_45_officer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["french_hussar_bearskin_officer", "Hussar Bearskin", [("french_hussar_bearskin_officer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["french_artillery_train_shako", "Artillery Train Shako", [("french_artillery_train_shako",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["french_nappy_hat", "Tokugaiemitsu's Helmet", [("Blueblood_Suji_Bachi_Kabuto_Crest1_Tokugawa",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(1.5)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["grach_bearskin_ranker", "Uma-Yumi Helmet", [("gekokujo_kabuto1_h_1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["grach_bearskin_officer", "GUma-Yumi Helmet", [("gekokujo_kabuto1_m_1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["grach_bearskin_trumpeter", "Grenadiers a Cheval Bearskin", [("grach_bearskin_trumpeter",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["french_captain_hat", "Japanese_captain_hat", [("kabuto_base_takeda",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["french_marine_hat", "french_marine_hat", [("gekokujo_sugegasa",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["french_seaman_hat", "french_seaman_hat", [("french_seaman_hat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["french_seaman_hat_2", "french_seaman_hat_2", [("french_seaman_hat_2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["nanban_helmet1", "Nanban Helmet", [("gekokujo_kabuto_nanban_h_1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(1.5)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["nanban_helmet2", "Nanban Helmet", [("gekokujo_kabuto_nanban_h_2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(1.5)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["nanban_helmet3", "Nanban Helmet", [("gekokujo_kabuto_nanban_h_3",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(1.5)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["nanban_helmet4", "Nanban Helmet", [("gekokujo_kabuto_nanban_h_4",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(1.5)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["nanban_helmet5", "Nanban Helmet", [("gekokujo_kabuto_nanban_h_5",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(1.5)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["nanban_helmet6", "Nanban Helmet", [("gekokujo_kabuto_nanban_h_6",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(1.5)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["nanban_helmet7", "Nanban Helmet", [("gekokujo_kabuto_nanban_h_7",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(1.5)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["japanese_seaman_hat", "Japanese seaman hat", [("gekokujo_sugegasa",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],  

["japanese_ronin_hat", "Japanese ronin hat", [("sam_ronin_gasa",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],  

["japanese_ronin_hat2", "Japanese ronin hat", [("kasa_yamabush",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],  

["japanese_ronin_hat3", "Japanese ronin hat", [("kasa_zen_full",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],  

["japanese_headwarp1", "Japanese ronin hat", [("gekokujo_headwrap",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],  

["japanese_headwarp2", "Japanese ronin hat", [("gekokujo_headwrap_black",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],  

["ninja_headwarp1", "Ninja headwarp", [("renzhemianzhao",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 

["ninja_headwarp2", "Ninja headwarp", [("renzhemianzhao2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 

["chivalrous_hat", "Chivalrous hat", [("xiake",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 

["jap_mc_hat", "Japanese Mount archer hat", [("sam_yabusame",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 

["honda_helmet", "Honda helmet", [("benduokui",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(1.5)|abundance(100)|head_armor(45)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 

 #Austrian
["aus_arty_bicorn", "Artillery Bicorne", [("aus_arty_bicorn",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["aus_arty_cap_bicorn", "Artillery Bicorne", [("aus_arty_cap_bicorn",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["aus_arty_train_hat", "Artillery Train Hat", [("aus_arty_train_hat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["aus_cavalry_helmet_officer", "Cavalry Helmet", [("aus_cavalry_helmet_officer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["aus_cavalry_helmet_ranker", "Cavalry Helmet", [("aus_cavalry_helmet_ranker",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["aus_cavalry_helmet_trumpeter", "Cavalry Helmet", [("aus_cavalry_helmet_trumpeter",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["aus_uhlan_czapka", "Uhlan Czapka", [("aus_uhlan_czapka",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["aus_uhlan_czapka_officer", "Uhlan Czapka", [("aus_uhlan_czapka_officer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["aus_uhlan_czapka_trumpeter", "Uhlan Czapka", [("aus_uhlan_czapka_trumpeter",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["aus_shwarzenberg_bicorn", "Schwarzenberg's Bicorne", [("aus_shwarzenberg_bicorn",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["aus_grenadier_bearskin", "Grenadier Bearskin", [("aus_grenadier_bearskin",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["aus_tyrol_hat", "Tyrol Hat", [("aus_tyrol_hat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["aus_tyrol_hat_officer", "Tyrol Hat", [("aus_tyrol_hat_officer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["aus_pioneer_hat", "Pioneer Hat", [("aus_pioneer_hat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["aus_grenadier_bearskin_officer", "Grenadier Bearskin", [("aus_grenadier_bearskin_officer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["aus_grenzer_officer", "Grenz Shako", [("aus_grenzer_officer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["aus_grenzer_ranker", "Grenz Shako", [("aus_grenzer_ranker",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["aus_infantry_nco", "Infantry Shako", [("aus_infantry_nco",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["aus_infantry_officer", "Infantry Shako", [("aus_infantry_officer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["aus_infantry_ranker", "Infantry Shako", [("aus_infantry_ranker",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["aus_hussard_shako_nco", "Hussar Shako", [("aus_hussard_shako_nco",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["aus_hussard_shako_officer", "Hussar Shako", [("aus_hussard_shako_officer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["aus_hussard_shako_ranker", "Hussar Shako", [("aus_hussard_shako_ranker",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["aus_hussard_shako_trumpeter", "Hussar Shako", [("aus_hussard_shako_trumpeter",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["aus_surgeon_hat", "Surgeon Hat", [("austria_surgeon_hat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["russian_cotton_cap", "Russian cotton cap", [("sha_e_min_bing_cap",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["russian_pike_man_cap", "Russian pike man cap", [("2kabasset",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["russian_pike_man_officer_cap", "Russian pike man officer cap", [("fxszjbbzg",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["russian_firelock_man_cap", "Russian firelock man cap", [("ukr_shapka_serduka",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["russian_firelock_man_officer_cap", "Russian firelock man officer cap", [("ukr_shapka_s_perom_b",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["stelz_soldier_hat", "stelz soldier hat", [("mosk_shishak",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["stelz_soldier_hat2", "stelz soldier hat", [("high_fur_cap_b",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 

["stelz_soldier_hat3", "stelz soldier hat", [("moher",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 

["stelz_officer_hat", "stelz officer hat", [("mosk_shishak",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["tsar_pro_army_helmet", "Tsar pro-army helmet", [("rus_morion_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["tsar_pro_army_helmet_officer", "Tsar pro-army helmet officer", [("xbytgaka",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["hats_of_russian_hussars", "Hats of Russian hussars", [("mosk_hat_streletz_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["hats_of_russian_hussars_officer", "Hats of Russian hussars officer", [("piaoqibingjunguanmao",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["raether_pistol_cavalry_helmet", "Raether pistol cavalry helmet", [("rus_reytar_helm",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["raether_pistol_cavalry_helmet_officer", "Raether pistol cavalry helmet officer", [("reytar_sholom",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["boyar_noble_cavalry_helmet", "Boyar noble cavalry helmet", [("misurka_c",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["boyar_noble_cavalry_helmet_officer", "Boyar noble cavalry helmet officer", [("mosk_shishak",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["opry_helmet", "Opry helmet", [("cav_cap_b",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["opry_helmet_officer", "Opry helmet", [("cav_cap_c",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["romanov_helmet", "Romanov helmet", [("misurka_rich_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(40)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    


#British
["british_artillery_shako_officer", "Artillery Shako", [("british_artillery_shako_officer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_artillery_shako_ranker", "Artillery Shako", [("british_artillery_shako_ranker",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_rocket_tarleton", "Artillery Tarleton", [("british_rocket_tarleton",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_kgl_shako_officer", "Ming Melee Infantry Officer helmet", [("DaMing_helmet_02",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(1.5)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_kgl_shako_ranker", "Ming Melee Infantry helmet", [("DaMing_helmet_06",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(1.5)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_light_shako_ranker", "Ming Shanwen Helmet", [("s_kuei3",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(2.25)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_light_shako_officer", "Ming Head warp", [("toujing_head",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_rifle_shako_officer", "Ming Musketeer Helmet", [("qibingkuei1",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(2.25)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],        
["british_rifle_shako_ranker", "Ming Musketeer Helmet", [("mingkuei2",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(2.25)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],     
["british_highland_bonnet_ranker", "Ming spearman helmet", [("SONG_BUBING_TOUKUI",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(2.25)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_highland_bonnet_ensign", "Highlander Bonnet", [("british_highland_bonnet_ensign",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_highland_bonnet_officer", "Ming Qinliangyu", [("SONG_QIBING",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_covers_head ,0, 4 , weight(2.25)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_highland_bonnet_drummer", "Ming hair", [("toujing_head",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.3)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_guard_shako_officer", "Ming hair", [("fabing_head",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.3)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_guard_shako_ranker", "Ming hair", [("copy_wamgjin_14",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.3)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["weisuo_helmet", "Weisuo Officer Helmet", [("s_kuei",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(1.5)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_lightdragoon_shako_ranker", "Ming dragoon helmet", [("DaMing_helmet_15",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(1.5)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_lightdragoon_shako_officer", "Ming heavy helmet", [("DaMing_helmet_02",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(2.5)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_lightdragoon_shako_trumpeter", "Light Dragoon Shako", [("british_23rd_lightdragoon_shako_trumpeter",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_iniskilling_helmet_ranker",  "Ming light hat", [("DaMing_helmet_17",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_iniskilling_helmet_officer", "Ming light hat", [("DaMing_helmet_17",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_iniskilling_helmet_trumpeter", "Dragoon Helmet", [("british_iniskilling_helmet_trumpeter",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair|itp_attach_armature  ,0, 4 , weight(0.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["british_lifeguard_helmet_ranker", "Ming Cotton Helmet", [("qibingkuei1",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(2.0)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_lifeguard_helmet_officer", "Ming Cotton Helmet Officer", [("qibingkuei1",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(2.0)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_lifeguard_helmet_trumpeter", "Horse Guard Helmet", [("british_lifeguard_helmet_trumpeter",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_kgl_hussar_bearskin", "Ming hussar helmet", [("DaMing_helmet_05",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_kgl_hussar_officer_bearskin", "KGL Hussar Helmet", [("KGL_hussar_officer_bearskin",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_kgl_hussar_bearskin_trumpeter", "KGL Hussar Helmet", [("KGL_hussar_bearskin_trumpeter",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_wellington_bicorne", "Ming Emperor helmet", [("WanLi03",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(1.5)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_captain_hat", "british_captain_hat", [("british_captain_hat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_seaman_hat", "british_seaman_hat", [("british_seaman_hat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_seaman_hat_2", "british_seaman_hat_2", [("british_seaman_hat_2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["royal_marine_beret", "Ming hat", [("toujing_head2",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["royal_marine_hat", "Ming Officer Hat", [("MWuShamao01",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["british_surgeon_bicorne", "Surgeon Bicorne", [("china_hat_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["minghat", "Ming hat", [("zhanmao",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.3)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["morion_a", "Morion", [("16thcombed_morion_blued",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.35)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["morion_b", "Morion", [("rus_morion_b",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.35)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["morion_c", "Morion", [("rus_morion_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.3)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["women_head1", "Women Head", [("3maid_of_honor",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_covers_head  ,0, 
4 , weight(0.3)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],  

["women_head2", "Women Head", [("3maid_of_honor",0)], itp_merchandise| itp_type_head_armor |itp_civilian |itp_covers_head ,0, 
4 , weight(0.3)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],  

["women_head3", "Women Head", [("maid_of_honor",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_covers_head  ,0, 
4 , weight(0.3)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],  

["women_head4", "Women Head", [("2_maid_of_honor",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_covers_head  ,0, 
4 , weight(0.3)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],  

["princess_appearance", "Princess appearance", [("2_maid_of_honor",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_covers_head  ,0, 
4 , weight(0)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],  


#Prussian
["prussian_landwehr_hat", "Landwehr Hat", [("landwehr_hat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_landwehr_hat_2", "Landwehr Hat", [("landwehr_hat_2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_landwehr_hat_3", "Landwehr Hat", [("landwehr_leather_hat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_shako", "Shako", [("prussian_shako",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_shako_2", "Drum hat", [("drummerhat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_infantry_hat_officer", "Officer Cap", [("prussian_8th_officer_hat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_hussar_shako", "Hussar Shako", [("prussian_deadhussars_shako",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_hussar_officer_shako", "Hussar Shako", [("prussian_hussar_officer_shako",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_blucher_hat", "Blucher's Cap", [("prussian_bluecher_hat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_arty_shako_officer", "Artillery Shako", [("prussian_arty_officer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_arty_shako_ranker", "Artillery Shako", [("prussian_arty_ranker",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_dragoon_shako_officer", "Dragoon Shako", [("prussian_dragoon_officer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_dragoon_shako_ranker", "Dragoon Shako", [("prussian_dragoon_ranker",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_guard_musician_shako", "Guard Infantry Shako", [("prussian_guard_musician_shako",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_guard_colours_shako", "Guard Infantry Shako", [("prussian_guard_NCO_shako",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_guard_officer_shako", "Guard Infantry Shako", [("prussian_guard_officer_shako",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_guard_ranker_shako", "Guard Infantry Shako", [("prussian_guard_ranker_shako",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_inf_off_shako", "Infantry Shako", [("officere1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_jaeger_officer_shako", "Jaeger Shako", [("prussian_jaeger_officer_shako",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.5)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_landwehr_cav_shako", "Landwehr Shako", [("prussian_landwer_cav",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_landwehr_cav_shako_officer", "Landwehr Shako", [("prussian_landwer_cav_officer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_pioneer_shako", "Pioneer Shako", [("prussian_pioneer_shako",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_shako_colours", "Infantry Shako", [("prussian_shako_proper_NCO",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_shako_colours_2", "Infantry Shako", [("prussian_shako_style_2_NCO",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_cuirassier_helmet", "Cuirassier Helmet", [("prussian_cuirassier_helmet",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_cuirassier_helmet_trumpet", "Cuirassier Helmet", [("prussian_cuirassier_helmet_trumpeter",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["prussian_freikorps_officer_hat", "Freikorps Hat", [("lutzov_off_hat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    #patch1115 25/1
["prussian_infantry2_hat", "Infantry Cap", [("23_fourage_hat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    #patch1115 25/2

["morion_d", "Morion", [("oim_p_roundhead_helmet",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.3)|abundance(100)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],  

["swordman_helmet", "Helmet", [("lobster5",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.35)|abundance(100)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["spa_hat1", "Spanish hat", [("1combed_morion_blued1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    

["spa_hat2", "Spanish hat", [("1combed_morion_blued",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 

["royal_guard_hat0", "Royal Guard hat", [("toukui6",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(3)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 

["royal_guard_hat1", "Royal guard officer hat", [("toukui5",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(3)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["shlapa_blue_a", "Light cavalry cap", [("drummerhat1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["shlapa_brown_b", "Light cavalry officer cap", [("drummerhat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(3)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["vaeg_capb", "Dragon cavalry officer cap", [("shlapa_blue_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(3)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["vaeg_cap", "Dragon cavalry officer cap", [("shlapa_brown_b",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(3)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["classichelm_plume", "Dragon cavalry officer cap", [("armetretxold3",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(5)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["classichelm_v_2", "Dragon cavalry cap", [("classichelm_v_2",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 
4 , weight(5)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["caijueqs", "Dragon cavalry officer cap", [("blacked_papenhaimer_plume",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(5)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["kettlehat", "Dragon cavalry cap", [("blacked_helmet",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(5)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["jaguar_helmet_4", "Dragon cavalry cap", [("jaguar_helmet_4",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["16ttoukui05", "Inca bronze helmet", [("16ttoukui05",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["16ttoukui05", "Inca bronze helmet", [("16ttoukui05",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["haijunzhangguan", "Commander of invincible fleet", [("haijunzhangguan",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["wudijianduichuanyuan", "Commander of invincible fleet", [("kettlehat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(3)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["feilisishidenaodai", "Philip IV's head", [("ofcer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
#Russian
["rus_opol_hat_ranker", "Opolocheniye Hat", [("qingkuei3",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["rus_opol_hat_officer", "Opolocheniye Hat", [("qingkuei1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["khergit_lady_hat", "Khergit Lady Hat", [("khergit_lady_hat",0)],  itp_type_head_armor   |itp_civilian |itp_doesnt_cover_hair | itp_fit_to_head,0, 
1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
#Rhine
["bavarian_helmet_other_ranks", "bavarian_helmet_other_ranks", [("bavarian_helmet_other_ranks",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["bavarian_helmet_flagcarrier", "bavarian_helmet_flagcarrier", [("bavarian_helmet_flagcarrier",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["bavarian_helmet_officer", "bavarian_helmet_officer", [("bavarian_helmet_officer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["bavarian_jaeger_helmet_other_ranks", "Jaeger Helmet", [("bavarian_jaeger_helmet_other_ranks",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["bavarian_jaeger_helmet_officer", "Jaeger Helmet", [("bavarian_jaeger_helmet_officer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["bavarian_helmet_artillery", "Artillery Helmet", [("bavarian_helmet_artillery_other_ranks",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["bavarian_helmet_train", "Artillery Helmet", [("bavarian_helmet_train_other_ranks",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["bavarian_helmet_artillery_officer", "Artillery Helmet", [("bavarian_helmet_artillery_officer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["saxon_inf_shako_ranker", "Infantry Shako", [("saxon_infantry_shako_private",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["saxon_inf_shako_nco", "Infantry Shako", [("saxon_infantry_shako_nco",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["saxon_inf_shako_officer", "Infantry Shako", [("saxon_infantry_shako_officer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["saxon_uhlan_shako_ranker", "Cavalry Shako", [("saxon_ulan_shako_private",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["saxon_uhlan_shako_ranker_alt", "Cavalry Shako", [("saxon_ulan_shako_private_2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["saxon_uhlan_shako_nco", "Cavalry Shako", [("saxon_ulan_shako_NCO",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["saxon_uhlan_shako_officer", "Cavalry Shako", [("saxon_ulan_shako_officer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["saxon_uhlan_shako_trumpeter", "Cavalry Shako", [("saxon_ulan_shako_trumpeter",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["hessian_inf_shako_ranker", "Infantry Shako", [("hessen_infantry_shako_private",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["hessian_inf_shako_nco", "Infantry Shako", [("hessen_infantry_shako_nco",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["hessian_inf_bicorne_officer", "Infantry Bicorne", [("hessen_infantry_officer_bicorn",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["rhine_surgeon_hat", "Surgeon Hat", [("rhine_surgeon_hat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["westphalian_hat_ranker", "Bearskin", [("west_gr_hat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["westphalian_hat_officer", "Bearskin", [("west_gr_off_hat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["saxonyking_hat", "Friedrich August Hat", [("saxonyking_hat",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["nassau_jaeger_hat_ranker", "Bearskin", [("nassau_ranker_hat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["nassau_jaeger_hat_officer", "Bearskin", [("nassau_off_hat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["wurttemberg_helmet_other_ranks", "wurttemberg_helmet_other_ranks", [("wurttemberg_helmet_private",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["wurttemberg_helmet_flagcarrier", "wurttemberg_helmet_flagcarrier", [("wurttemberg_helmet_NCO",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["wurttemberg_helmet_officer", "wurttemberg_helmet_officer", [("wurttemberg_helmet_officer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["wurttemberg2_helmet_other_ranks", "wurttemberg_helmet_other_ranks", [("wurttemberg_helmet_grenadier",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["wurttemberg2_helmet_flagcarrier", "wurttemberg_helmet_flagcarrier", [("wurttemberg_helmet_grenadier_NCO",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["wurttemberg2_helmet_officer", "wurttemberg_helmet_officer", [("wurttemberg_helmet_grenadier_officer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["berg_pioneer_bearskin", "Bearskin", [("berg_pioneer_bearskin",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["saxon_helmet_other_ranks", "saxon_helmet_other_ranks", [("helmet_garde_du_corps",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["saxon_helmet_flagcarrier", "saxon_helmet_flagcarrier", [("helmet_garde_du_corps_nco",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["saxon_helmet_officer", "saxon_helmet_officer", [("helmet_garde_du_corps_officer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["saxon_helmet_trumpeter", "saxon_helmet_officer", [("helmet_garde_du_corps_trumpeter",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["westphalian_helmet_other_ranks", "westphalian_helmet_other_ranks", [("westphalian_cuirassier_helmet_private",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["westphalian_helmet_flagcarrier", "westphalian_helmet_flagcarrier", [("westphalian_cuirassier_helmet_NCO",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["westphalian_helmet_officer", "westphalian_helmet_officer", [("westphalian_cuirassier_helmet_officer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["westphalian_helmet_trumpeter", "westphalian_helmet_officer", [("westphalian_cuirassier_helmet_trumpeter",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["badner_helmet_flagcarrier", "badner_helmet_flagcarrier", [("baden_dragoon_helmet_NCO",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["badner_helmet_officer", "badner_helmet_officer", [("baden_dragoon_helmet_officer",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["badner_helmet_ranker", "badner_helmet_officer", [("baden_dragoon_helmet_private",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["badner_helmet_trumpeter", "badner_helmet_officer", [("baden_dragoon_helmet_trumpeter",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],  

["osman_hat", "Osman hat", [("turban12",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 

["osman_hat_officer", "Osman hat", [("turban",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 

["chichak_helmet", "Chichak helmet", [("ghulam_at",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 

["osman_shooter_hat", "Osman shooter hat", [("ttr_kolpak",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["sultan_hat", "Sultan hat", [("solak",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 

["sultan_hat_officer", "Sultan hat officer", [("yeni_bork_1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 

["holy_warrior_hat", "Holy warrior hat", [("haoshuaodsmtj",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 

["turkmen_cavalry_helmet", "Turkmen cavalry helmet", [("damombined",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 

["gorgeous_chichak_helmet", "Gorgeous Chichak helmet", [("hasakejiangjuntokui",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 

["mamluk_helmet", "Mamluk helmet", [("sar_helmet4",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(1.8)|abundance(100)|head_armor(35)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 

["pirate_headscarf_a", "Pirate headscarf", [("hitmen_bandana_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 

["pirate_headscarf_b", "Pirate headscarf", [("hitmen_bandana_v",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 

["deni_apza_navy_cap", "Deni Apza Navy Cap", [("pol_hat_simple",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 

["deni_apza_navy_officer_cap", "Deni Apza Navy Cap officer", [("hat-blue",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],

["guards_artillery_cap", "Guards artillery cap", [("hat-blue_bing",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 

["guards_artillery_cap_officer", "Guards artillery cap officer", [("hat-blue",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],  

["engineer_hat", "Engineer hat", [("albmz",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],  

["muslim_long_crown", "Muslim long crown", [("turban3",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],  
#poland
["dada1", "dada1", [("old_turban_helmet_b",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["dada2", "dada2", [("turban_helmet_b",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["dada3", "dada3", [("turban_helmet_c",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(25)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["dada4", "dada4", [("old_kula_hud_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["dada5", "dada5", [("kula_hud_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(17)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["dada6", "dada6", [("chan_kula_hud_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(17)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["yiqibingtoukui1", "yiqibingtoukui1", [("old_turkish_helmet_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(27)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["yiqibingtoukui2", "yiqibingtoukui2", [("turkish_helmet_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(27)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["yiqibingtoukui3", "yiqibingtoukui3", [("turkish_helmet_b",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(27)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["yiqibingtoukui4", "yiqibingtoukui4", [("turkish_helmet_b1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["yiqibingtoukui5", "yiqibingtoukui5", [("turkish_helmet_c",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(33)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["yiqibingtoukui6", "yiqibingtoukui6", [("turkish_helmet_d",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["yiqibingtoukui7", "yiqibingtoukui7", [("turkish_helmet_e",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["yiqibingtoukui8", "yiqibingtoukui8", [("jerychonka_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(29)|body_armor(1)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["yiqibingtoukui9", "yiqibingtoukui9", [("jerychonka_b",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(29)|body_armor(1)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["yiqibingtoukui10", "yiqibingtoukui10", [("blacked_papenhaimer_plume.1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(30)|body_armor(1)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["yiqibingtoukui11", "yiqibingtoukui11", [("papenhaimer_plume.1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(30)|body_armor(1)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["yiqibingtoukui12", "yiqibingtoukui12", [("black_papenhaimer_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(27)|body_armor(1)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["yiqibingtoukui13", "yiqibingtoukui13", [("old_black_papenhaimer_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(27)|body_armor(1)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["yiqibingtoukui14", "yiqibingtoukui14", [("black_papenhaimer_b",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(27)|body_armor(1)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bubingkui1", "bubingkui1", [("blacked_burgonet_plume.1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bubingkui2", "bubingkui2", [("burgonet_plume.1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bubingkui3", "bubingkui3", [("burgonet_a0",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(13)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bubingkui4", "bubingkui4", [("burgonet_a1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(13)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bubingkui5", "bubingkui5", [("burgonet_a2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(13)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bubingkui6", "bubingkui6", [("burgonet_b1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(13)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bubingkui7", "bubingkui7", [("burgonet_b2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(13)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sheshoumao1", "sheshoumao1", [("cabasset_ab",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sheshoumao2", "sheshoumao2", [("cabasset_aa",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sheshoumao3", "sheshoumao3", [("cabasset_bb",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["sheshoumao4", "sheshoumao4", [("cabasset_ch.1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bubing1", "bubing1", [("swe_morion_ba",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bubing2", "bubing2", [("swe_morion_bb",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bubing3", "bubing3", [("old_rus_morion_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bubing4", "bubing4", [("rus_morion_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bubing5", "bubing5", [("rus_morion_b",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bubing6", "bubing6", [("szlom_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bubingzhongkui1", "bubingzhongkui1", [("old_hussar_capalin_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bubingzhongkui2", "bubingzhongkui2", [("hussar_capalin_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["qishikui1", "qishikui1", [("hussar_helmet_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["qishikui2", "qishikui2", [("hussar_helmet_b",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["qishikui3", "qishikui3", [("hussar_helmet_c",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2)|abundance(100)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["nengmin1", "nengmin1", [("sailor_hat_a1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.2)|abundance(100)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["nengmin2", "nengmin2", [("sailor_hat_a2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.2)|abundance(100)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["nengmin3", "nengmin3", [("sailor_hat_a3",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.2)|abundance(100)|head_armor(3)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["nengmin4", "nengmin4", [("se_bandana_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["nengmin5", "nengmin5", [("rp_bandana_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["gskm1", "gskm1", [("high_fur_cap_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(7)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["gskm2", "gskm2", [("cossac_hat_a2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(7)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["gskm3", "gskm3", [("cossac_hat_a3",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(7)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["gskm4", "gskm4", [("cossac_hat_a4",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(7)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["gskm5", "gskm5", [("high_fur_cap_b",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["gskm6", "gskm6", [("moher",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["gskm7", "gskm7", [("bohunhat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["minbingmaozi1", "minbingmaozi1", [("magierka_a1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.2)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["minbingmaozi2", "minbingmaozi2", [("rp_kolpak_a0",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.2)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["minbingmaozi3", "minbingmaozi3", [("rp_kolpak_a1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.2)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["minbingmaozi4", "minbingmaozi4", [("rp_kolpak_a2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.2)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["minbingmaozi5", "minbingmaozi5", [("rp_kolpak_a3",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.2)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["minbingmaozi6", "minbingmaozi6", [("hrv_hat_a0.0",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.2)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["minbingmaozi7", "minbingmaozi7", [("hrv_hat_a1.0",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.2)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["minbingmaozi8", "minbingmaozi8", [("hrv_hat_b1.0",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.2)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["minbingmaozi9", "minbingmaozi9", [("hrv_hat_b2.0",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.2)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["gskqbm1", "gskqbm1", [("rp_kolpak_b0.0",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["gskqbm2", "gskqbm2", [("rp_kolpak_b1.0",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["gskqbm3", "gskqbm3", [("rp_kolpak_b2.0",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["gskqbm4", "gskqbm4", [("rp_kolpak_b3.0",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["gskqbm5", "gskqbm5", [("rp_kolpak_b4.0",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["gskqbm6", "gskqbm6", [("-rp_kolpak_b4.0",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["gskqbm7", "gskqbm7", [("rp_kolpak_b5.0",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["gskqbm8", "gskqbm8", [("rp_kolpak_b6.0",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["gskqbm9", "gskqbm9", [("rp_kolpak_ch0",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["gskqbm10", "gskqbm10", [("rp_kolpak_ch1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blmbm1", "blmbm1", [("rp_kolpak_o0",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.1)|abundance(100)|head_armor(1)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blmbm2", "blmbm2", [("rp_kolpak_o1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blmbm3", "blmbm3", [("rp_kolpak_o2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blmbm4", "blmbm4", [("rp_kolpak_o3",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blmbm5", "blmbm5", [("rs_kolpak_a2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blmbm6", "blmbm6", [("rb_kolpak_na1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blmbm7", "blmbm7", [("gs_kolpak_na2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blmbm8", "blmbm8", [("bbr_kolpak_na3",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blmbm9", "blmbm9", [("rbr_kolpak_nb1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blmbm10", "blmbm10", [("bs_kolpak_nb1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blmbm11", "blmbm11", [("gb_kolpak_nb1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blmbm12", "blmbm12", [("rb_kolpak_nd1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blmbm13", "blmbm13", [("gbr_kolpak_nd1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bldgm1", "bldgm1", [("wall_cap_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(1)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bldgm2", "bldgm2", [("wall_cap_b",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(1)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bldgm3", "bldgm3", [("wall_cap_c",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(1)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bldgm4", "bldgm4", [("wall_cap_d",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(1)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bldgm5", "bldgm5", [("wall_cap_e",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(1)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blxm1", "blxm1", [("soldats_cap_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blxm2", "blxm2", [("soldats_cap_a2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blxm3", "blxm3", [("strelets_cap_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blxm4", "blxm4", [("strelets_cap_a2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blxm5", "blxm5", [("strelets_cap_a3",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blxm6", "blxm6", [("strelets_cap_a4",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blxm7", "blxm7", [("muscov_off_cap_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blzzm1", "blzzm1", [("cav_cap_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(1.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blzzm2", "blzzm2", [("cav_cap_b",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(1.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blzzm3", "blzzm3", [("cav_cap_c",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(1.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blzzm4", "blzzm4", [("cav_cap_d",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(1.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blzzm5", "blzzm5", [("guard_cav_cap_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(1.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blzzm6", "blzzm6", [("guard_cav_cap_b",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(1.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blzzm7", "blzzm7", [("guard_cav_cap_c",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(1.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blzzm8", "blzzm8", [("guard_cav_cap_d",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(1.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["gskxm1", "gskxm1", [("deli_cap_b",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["gskxm2", "gskxm2", [("deli_cap_c",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blysm1", "blysm1", [("deli_cap_e",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blysm2", "blysm2", [("deli_cap_d",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["gskxm3", "gskxm3", [("azab_cap_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["gskxm4", "gskxm4", [("azab_cap_b",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["gskxm5", "gskxm5", [("turban1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["gskxm6", "gskxm6", [("turban2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["gskxm7", "gskxm7", [("turban3",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bljdxm1", "bljdxm1", [("turban_helmet_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bljdxm2", "bljdxm2", [("turban_helmet_a2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bljdxm3", "bljdxm3", [("flagman_turban_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bljdxm4", "bljdxm4", [("tufekci",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(7)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bljdxm5", "bljdxm5", [("tufekci1",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(7)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bljdxm6", "bljdxm6", [("tufekci2",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(7)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["bljdxm7", "bljdxm7", [("tufekci3",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(7)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blmbcsm1", "blmbcsm1", [("tartan_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blmbcsm2", "blmbcsm2", [("tartan_b",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blyqbzzm1", "blyqbzzm1", [("husar_sholom",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2.5)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["blyqbzzm2", "blyqbzzm2", [("pol_husar_helm_greben",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 
4 , weight(2.5)|abundance(100)|head_armor(44)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
#Pirate
["pirate_hat", "Pirate Hat", [("pirate_hat",0)], itp_merchandise| itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
#腿甲
#Boots
 #French
 ["french_voltigeur_pants", "Japanese Sandal", [("gekokujo_sandal_1",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
 ["french_voltigeur_officer_pants", "Japanese Sandal", [("gekokujo_sandal_2",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
 ["french_dragoon_pants", "Japanese Sandal", [("gekokujo_sandal_3",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
 ["french_general_boots", "General's Boots", [("gekokujo_jinbaori_tokugawa",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["french_grenadiers_a_cheval_pants", "Jap Cavalry Boots", [("gekokujo_tsubo_suneate_2",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["french_vistula_pants", "Hessian Boots", [("french_vistula_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["french_lancer_pants", "Monk Pants", [("gekokujo_shino_suneate_1",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["french_lancer_officer_pants", "Monk Pants", [("gekokujo_shino_suneate_1",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["french_hussards_ranker_pants", "Cavalry Pants", [("french_hussards_ranker_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["french_hussards_officer_pants", "Cavalry Pants", [("french_hussards_officer_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["french_hussards_trumpeter_pants", "Cavalry Pants", [("french_hussards_trumpeter_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["french_sappeur_pants", "Suneate", [("gekokujo_light_suneate_1",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["french_art_ranker_pants", "Artillery Gaiters", [("french_art_ranker_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["french_GRaP_pants", "Oda suneate", [("gekokujo_shino_suneate_1",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["fr_arty_captain_bottefortes", "Artillery Boots", [("fr_arty_captain_bottefortes",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["fr_arty_train_bottefortes", "Artillery Boots", [("fr_arty_train_bottefortes",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["fr_officer_bottefortes", "Officer Boots", [("fr_officer_bottefortes",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["french_captain_pants", "Officer Boots", [("french_captain_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["french_basic_infantry_pants", "Infantry Boots", [("gekokujo_light_suneate_1",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
 ["french_captain_pants_blue", "Officer Boots", [("french_captain_pants_blue",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["french_equipage_batallion_pants", "Infantry Boots", [("french_equipage_batallion_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["french_sailor_pants", "Infantry Boots", [("french_sailor_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(4.5)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(36)|difficulty(0) ,imodbits_cloth ], #patch1115 23/1
 ["french_sailor_pants_female", "Infantry Boots", [("french_sailor_pants_fem",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(4.5)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(36)|difficulty(0) ,imodbits_cloth ], #patch1115 23/2
 ["french_surgeon_pants", "Surgeon Pants", [("french_surgeon_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 
 ["suneate_g", "Suneate", [("gekokujo_light_suneate_2",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],

 ["suneate_r", "Suneate", [("gekokujo_tsubo_suneate_3",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 
 ["ninja_boot", "Ninja boot", [("BlackNinjaBoots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
 
["fysg_bin_shazei01_t", "fysg_bin_shazei01_t", [("fysg_bin_shazei01_t",0)], itp_merchandise| itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 80 , weight(0.5)|abundance(110)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
 
 ["honda_boots", "Officer Boots", [("benduoxie",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(40)|difficulty(0) ,imodbits_cloth ],
 
 #Russian
 ["rus_infantry_pants1", "Qing Salve Pants", [("turk_boots_b",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian ,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["rus_infantry_pants2", "Infantry Boots", [("rus_musketeer_pants2",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["rus_hussar_pants1", "Cavalry Gaiters", [("rus_hussar_pants1",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["rus_hussar_pants2", "Cavalry Gaiters", [("rus_hussar_pants2",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["rus_hussar_pants_nco", "Hussar Hessians", [("nomad_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["rus_hussar_pants_officer", "Hussar Hessians", [("rus_hussards_off_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["rus_horse_guard_pants", "Cavalry Boots", [("rus_chevalier_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["rus_cossack_off_pants", "Cossack Pants", [("rus_cossack_off_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["rus_kutuzov_pants", "General's Boots", [("rus_kutuzov_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["rus_militia_off_pants", "Militia Boots", [("rus_militia_off_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["rus_militia_ranker_pants", "Militia Boots", [("rus_militia_ranker_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["rus_militia_ranker_pants1", "Militia Pants", [("rus_militia_ranker_pants1",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["rus_jaeger_pants", "Jaeger Boots", [("rus_jaeger_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["rus_arty_pants", "Artillery Boots", [("rus_arty_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["rus_dragoon_pants1", "Cavalry Gaiters", [("rus_dragoon_pants1",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["rus_dragoon_pants2", "Cavalry Gaiters", [("rus_dragoon_pants2",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["rus_uhlan_pants", "Cavalry Pants", [("russian_uhlan_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["khergit_leather_boots", "Khergit Leather Boots", [("khergit_leather_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 120 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_cloth ],
 ["qing_pants", "Qing Pants", [("kuzi_c",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 120 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
 
 #Austrian
 ["austrian_infantry_pants", "Infantry Boots", [("austrian_infantry_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["hungarian_pants", "Infantry Shoes", [("austrian_hungarian_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["hungarian_pants_officer", "Infantry Boots", [("austrian_hungarian_officer_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["austrian_jaeger_pants", "Jaeger Boots", [("austrian_jaeger_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["austrian_jaeger_pants_officer", "Jaeger Boots", [("austrian_jaeger_officer_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["hungarian_hussar_pants", "Hussar Hessians", [("austrian_hussard_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["hungarian_uhlan_pants", "Hussar Hessians", [("austrian_uhlan_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["austrian_schwarzenberg_pants", "Schwarzenberg's Pants", [("schwarzenberg_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["austrian_officer_boots", "Infantry Boots", [("austrian_officer_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["austrian_cavalry_boots", "Cavalry Boots", [("austrian_cavalry_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 
 #British
 ["british_highland_kilt", "Kilt", [("british_highland_kilt",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["british_highland_kilt_2", "Kilt", [("british_highland_kilt_2",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["british_highland_kilt_officer", "Kilt", [("british_highland_kilt_officer",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["british_rifle_captain_pants", "Ming boots", [("Song_boot_d",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_cloth ],
 ["ming_boot", "Ming boot", [("DaMing_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
 ["british_coldstream_pants", "Infantry Pants", [("british_coldstream_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["british_sapper_pants", "Sapper Pants", [("British_sappeur_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["british_wellington_pants", "Wellington's Pants", [("wellington_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["british_light_dragoon_pants", "Light Dragoon Pants", [("british_light_dragoon_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["british_rocketeer_pants", "Cavalry Pants", [("british_rocketeer_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["british_cav_pants", "Cavalry Pants", [("british_cav_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["british_kgl_hussar_pants", "Cavalry Pants", [("KGL_hussar_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["british_kgl_hussar_officer_pants", "Cavalry Pants", [("KGL_hussar_officer_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["british_captain_legs", "british_captain_legs", [("british_captain_legs",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["sailor_pants", "sailor_pants", [("sailor_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(4.25)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(36)|difficulty(0) ,imodbits_cloth ], #patch1115 23/3
 ["sailor_pants_female", "sailor_pants_female", [("sailor_pants_fem",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(4.25)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(36)|difficulty(0) ,imodbits_cloth ], #patch1115 23/4
 ["western_boots", "Western Boots", [("infantry_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
 
 
 #Prussian
 ["prussian_infantry_pants", "Infantry Boots", [("sockshoes1",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["leather_boots_a", "Infantry Boots", [("blackcavboots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,#xiugai
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["prussian_landwehr_pants", "Landwehr Pants", [("prussian_landwehr_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["prussian_landwehr_pants2", "Landwehr Pants", [("prussian_landwehr_pants_2",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["prussian_blucher_pants", "Blucher's Pants", [("blucher_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["prussian_cavalry_pants", "Cavalry Pants", [("prussian_cavalry_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["prussian_cavalry_pants2", "Cavalry Pants", [("prussian_cavalry_pants2",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["prussian_hussar_pants", "Cavalry Boots", [("prussian_hussar_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["prussian_hussar_pants_officer", "Cavalry Hessians", [("prussian_hussar_officer_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["prussian_freikorps_pants", "Freikorps Pants", [("prussian_lutzov_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 
 ["firelockman_pants", "Infantry Boots", [("boot_pblack_blue",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_cloth ],
 
 ["royal_guard_pants", "Royal Guard pants", [("xie5",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(35)|difficulty(0) ,imodbits_cloth ],
 
 ["iron_greaves_a", "Royal Guard pants", [("iron_greaves_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(35)|difficulty(0) ,imodbits_cloth ],
 
 ["black_greaves", "black greaves", [("black_greaves",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_cloth ],
 
 ["jaguar_boots2", "black greaves", [("jaguar_boots2",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.0)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
 
 ["incan_boots", "Inca sandals", [("incan_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.0)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
 #Rhine
 ["bavarian_infantry_pants", "Infantry Boots", [("bavarian_infantry_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["bavarian_pants_officer", "Infantry Boots", [("bavarian_officer_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["bavarian_artillery_pants", "Artillery Pants", [("bavarian_artillery_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["bavarian_artillery_pants_officer", "Artillery Boots", [("bavarian_artillery_officer_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["saxon_uhlan_pants", "Cavalry Boots", [("saxon_ulan_other_rank_parade_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["saxon_uhlan_pants_alt", "Cavalry Boots", [("saxon_ulan_other_rank_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["saxon_uhlan_pants_officer", "Cavalry Boots", [("saxon_ulan_officer_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["hessian_infantry_pants", "Infantry Boots", [("hessen_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["hessian_infantry_pants_officer", "Infantry Boots", [("hessen_officer_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["nassau_jaeger_pants", "Cavalry Boots", [("nassau_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["nassau_jaeger_pants_officer", "Cavalry Boots", [("nassau_off_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["wurttemberg_pants_all_ranks", "Infantry Boots", [("wurttemberg_pants_all_ranks",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["wurttemberg_pants_officer", "Infantry Boots", [("wurttemberg_pants_officer",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["wurttemberg_grenadier_pants", "Infantry Boots", [("wurttemberg_grenadier_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["berg_pioneer_pants", "Infantry Boots", [("berg_pioneer_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["garde_du_corps_pants_ranker", "Cavalry Boots", [("garde_du_corps_pants_ranker",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["garde_du_corps_pants", "Cavalry Boots", [("garde_du_corps_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["baden_dragoon_pants", "Cavalry Boots", [("baden_dragoon_pants",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 
 ["osman_boot", "Cavalry Boots", [("sarranid_shoes",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
 
 ["chain_boots", "Chain boots", [("sarranid_mail_chausses",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
 
 ["osman_leather_boots", "Osman leather boots", [("sarranid_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
 
 ["saints_boots", "Saints boots", [("pixueaa",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
 
 ["chain_boots_with_cape", "Chain boots with cape", [("Pifeng02",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
 
 ["pirate_leg_protection", "Pirate leg protection", [("splinted_greaves_nospurs",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
 
 ["deni_apza_navy_boots", "Deni Apza navy boots", [("pixueaa",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
 
 ["deni_apza_navy_boots_off", "Deni Apza navy boots", [("turk_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.8)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
 
 ["leather_boots_with_cloak", "Leather boots with cloak", [("jinweipaobing_guan",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
 
 ["leather_boots_with_white_cloak", "Leather boots with white cloak", [("baipifeng",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
 
 
 #Tsarist Russia
 ["russian_gaiter", "Russian gaiter", [("ankle_boots_a_new",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],
 
 ["russian_leather_boots", "Russian leather boots", [("wrapping_boots_a3",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_cloth ],
 
 ["stelz_officer_boots", "Stelz officer boots", [("nomad_boots_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(25)|difficulty(0) ,imodbits_cloth ],
 
 ["raether_pistol_cavalry_boots", "Raether pistol cavalry boots", [("shouqiangqibing_boot",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(25)|difficulty(0) ,imodbits_cloth ],
 
 ["opry_boots", "Opry boots", [("shouqiangqibing_boot",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(35)|difficulty(0) ,imodbits_cloth ],
 
 ["streltsy_boots", "Streltsy boots", [("east_boots_2b",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(35)|difficulty(0) ,imodbits_cloth ],
 
 ["cav_boots", "Cavlary boots", [("rp_huss_boots_a0",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(10)|leg_armor(35)|difficulty(0) ,imodbits_cloth ],
 #poland
 ["bolanminbingxie_gaiter1", "bolanminbingxie_gaiter1", [("wrapping_boots_low",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
 ["bolanmengminxie_gaiter2", "bolanmengminxie_gaiter2", [("east_boots_light_low_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["bolanmengminxie_gaiter3", "bolanmengminxie_gaiter3", [("east_boots_light_low_b",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["bolanmengminxie_gaiter4", "bolanmengminxie_gaiter4", [("east_boots_light_low_c",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["bolanbubingxie_gaiter1", "bolanbubingxie_gaiter1", [("east_boots_heavy_low_a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["bolanbubingxie_gaiter2", "bolanbubingxie_gaiter2", [("east_boots_heavy_low_b",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(5)|difficulty(0) ,imodbits_cloth ], 
 ["bolanchangku_gaiter1", "bolanchangku_gaiter1", [("east_boots_0a",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(7)|difficulty(0) ,imodbits_cloth ], 
 ["bolanchangku_gaiter2", "bolanchangku_gaiter2", [("east_boots_1f",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(7)|difficulty(0) ,imodbits_cloth ], 
 ["bolanchangku_gaiter3", "bolanchangku_gaiter3", [("east_boots_1g",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(7)|difficulty(0) ,imodbits_cloth ], 
 ["bolanchangku_gaiter4", "bolanchangku_gaiter4", [("east_boots_1e",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(7)|difficulty(0) ,imodbits_cloth ], 
 ["bolanchangku_gaiter5", "bolanchangku_gaiter5", [("east_boots_1h",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(7)|difficulty(0) ,imodbits_cloth ], 
 ["bolanbubingku_gaiter6", "bolanbubingku_gaiter6", [("swedish_boots_a1",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(17)|difficulty(0) ,imodbits_cloth ], 
 ["bolanbubingku_gaiter7", "bolanbubingku_gaiter7", [("swedish_boots_a2",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(17)|difficulty(0) ,imodbits_cloth ], 
 ["bolanbubingku_gaiter8", "bolanbubingku_gaiter8", [("swedish_boots_a3",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(17)|difficulty(0) ,imodbits_cloth ], 
 ["bolanbubingku_gaiter9", "bolanbubingku_gaiter9", [("swedish_boots_a4",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(17)|difficulty(0) ,imodbits_cloth ], 
 ["bolanbubingku_gaiter11", "bolanbubingku_gaiter11", [("swedish_boots_b0",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(17)|difficulty(0) ,imodbits_cloth ], 
 ["bolanbubingku_gaiter12", "bolanbubingku_gaiter12", [("swedish_boots_b1",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(17)|difficulty(0) ,imodbits_cloth ], 
 ["bolanbubingku_gaiter13", "bolanbubingku_gaiter13", [("swedish_boots_b2",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(17)|difficulty(0) ,imodbits_cloth ], 
 ["bolanbubingku_gaiter14", "bolanbubingku_gaiter14", [("swedish_boots_b3",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(17)|difficulty(0) ,imodbits_cloth ], 
 ["bolanbubingku_gaiter15", "bolanbubingku_gaiter15", [("swedish_boots_b4",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(17)|difficulty(0) ,imodbits_cloth ], 
 ["bolanbubingku_gaiter16", "bolanbubingku_gaiter16", [("swedish_boots_c1",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(17)|difficulty(0) ,imodbits_cloth ], 
 ["bolanbubingku_gaiter17", "bolanbubingku_gaiter17", [("swedish_boots_c2",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(17)|difficulty(0) ,imodbits_cloth ], 
 ["bolanmaku_gaiter1", "bolanmaku_gaiter1", [("swedish_boots_off_a1",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_cloth ], 
 ["bolanmaku_gaiter2", "bolanmaku_gaiter2", [("swedish_boots_off_a2",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_cloth ], 
 ["bolanmaku_gaiter3", "bolanmaku_gaiter3", [("swedish_boots_off_a3",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_cloth ],
 ["bolanmaku_gaiter4", "bolanmaku_gaiter4", [("swedish_boots_off_a4",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(25)|difficulty(0) ,imodbits_cloth ],
 ["bolanshuibingku_gaiter1", "bolanshuibingku_gaiter1", [("swedish_boots_cav_a1",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_cloth ],
 ["bolanqishiku_gaiter2", "bolanqishiku_gaiter2", [("swedish_boots_cav_a2",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["bolanqishiku_gaiter3", "bolanqishiku_gaiter3", [("swedish_boots_cav_a3",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["bolanqishiku_gaiter4", "bolanqishiku_gaiter4", [("swedish_boots_cav_a4",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["bolanqishiku_gaiter5", "bolanqishiku_gaiter5", [("swedish_boots_cav_a5",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 ["bolanck_gaiter1", "bolanck_gaiter1", [("rp_boots_a0",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["bolanck_gaiter2", "bolanck_gaiter2", [("rp_boots_a2",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["bolanck_gaiter3", "bolanck_gaiter3", [("rp_boots_b0",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["bolanck_gaiter4", "bolanck_gaiter4", [("rp_boots_b1",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.2)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
 ["bolanck_gaiter5", "bolanck_gaiter5", [("gray_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 ["bolanck_gaiter6", "bolanck_gaiter6", [("brown_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 ["bolanck_gaiter7", "bolanck_gaiter7", [("black_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 ["bolanck_gaiter8", "bolanck_gaiter8", [("yellow_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 ["bolanck_gaiter9", "bolanck_gaiter9", [("red_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(0.3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
 ["bolanmk_gaiter1", "bolanmk_gaiter1", [("rp_huss_boots_a0",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
 ["bolanmk_gaiter2", "bolanmk_gaiter2", [("rp_huss_boots_a1",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
 ["bolanmk_gaiter3", "bolanmk_gaiter3", [("rp_huss_boots_b1",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
 ["bolanmk_gaiter4", "bolanmk_gaiter4", [("rp_huss_boots_b2",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
 ["winged_hussar_boots", "Winged Hussar Boots", [("sapogi_kavaleria_red",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 10 , weight(1.3)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(30)|difficulty(0) ,imodbits_cloth ],
 #手套
# Gloves
 ["officer_gloves","Officer Gloves", [("ssh_tekko_2_L",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(0)|abundance(100)|body_armor(0)|difficulty(0),imodbits_cloth],
 ["drummer_gloves","Drummer Gloves", [("drummer_gloves_L",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(0)|abundance(100)|body_armor(0)|difficulty(0),imodbits_cloth],
 ["rus_chevgarde_gloves","Gloves", [("mm_invisible_L",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(0)|abundance(100)|body_armor(0)|difficulty(0),imodbits_cloth],
 ["fr_cuirassier_gloves", "Gloves", [("fr_cavalry_glove_L",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(0)|abundance(100)|body_armor(0)|difficulty(0),imodbits_cloth],
 ["fr_artillery_gloves", "Gloves", [("glove_black_L",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(0)|abundance(100)|body_armor(0)|difficulty(0),imodbits_cloth],
 ["br_cavalry_gloves", "Gloves", [("white_cavalry_glove_L",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(0)|abundance(100)|body_armor(0)|difficulty(0),imodbits_cloth],
 ["br_horseguard_gloves", "Gloves", [("hg_cavalry_glove_L",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(0)|abundance(100)|body_armor(0)|difficulty(0),imodbits_cloth],
 ["br_cavalry_gloves_short", "Gloves", [("white_cavalry_glove_short_L",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(0)|abundance(100)|body_armor(0)|difficulty(0),imodbits_cloth],
 ["br_horseguard_gloves_short", "Gloves", [("hg_cavalry_glove_short_L",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(0)|abundance(100)|body_armor(0)|difficulty(0),imodbits_cloth],
 ["officer_gloves2", "Officer_Gloves", [("no_gloves_forkietL", 0)], itp_merchandise|itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand, 0, 0, weight(0.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(0), imodbits_none], 
 ["tekko","Tekko", [("gf_tekko_2_1_L",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(0)|abundance(100)|body_armor(5)|difficulty(0),imodbits_cloth],
 ["tekko2","Light Tekko", [("gf_tekko_1_L",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(0)|abundance(100)|body_armor(4)|difficulty(0),imodbits_cloth],
 ["tekko3","Tekko", [("ssh_tekko_1_R",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(0)|abundance(100)|body_armor(4)|difficulty(0),imodbits_cloth],
 ["tekko_g","Tekko", [("gf_tekko_2_2_R",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(0)|abundance(100)|body_armor(4)|difficulty(0),imodbits_cloth],
 ["tekko_r","Tekko", [("gf_tekko_2_3_R",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(0)|abundance(100)|body_armor(4)|difficulty(0),imodbits_cloth],
 ["tekko_b","Tekko", [("ssh_tekko_1_R",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(0)|abundance(100)|body_armor(4)|difficulty(0),imodbits_cloth],
 
 ["royal_guards_b","Tekko", [("zuoshou5_L",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(2)|abundance(100)|body_armor(5)|difficulty(0),imodbits_cloth],
 
 ["hourglass_gauntlets_r","Tekko", [("hourglass_gauntlets_R",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(2)|abundance(100)|body_armor(5)|difficulty(0),imodbits_cloth],
 
 ["chain_gloves","Chain gloves", [("mail_mittens_L",0)], itp_merchandise|itp_type_hand_armor,0, 90, weight(2)|abundance(100)|body_armor(5)|difficulty(0),imodbits_cloth],
 
 ["long_axe_frame_gun", "Long axe frame gun", [("berdish_L", 0)], itp_merchandise|itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand, 0, 0, weight(0.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(0), imodbits_none], 
 
 ["long_axe_frame_gun_guard", "Long axe frame gun", [("yuerenfujiaqiangpishoutao_L", 0)], itp_merchandise|itp_type_hand_armor|itp_force_show_left_hand|itp_force_show_right_hand, 0, 0, weight(0.000000)|abundance(100)|difficulty(0)|head_armor(0)|body_armor(0)|leg_armor(0), imodbits_none], 
#马
#Horses
 #French
 ["hussar_horse_french","Uma-Yumi Horse", [("zhanguoma",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(10)|hit_points(85)|difficulty(3)|horse_speed(42)|horse_maneuver(45)|horse_charge(22)|horse_scale(90),imodbits_horse_basic|imodbit_champion],
 ["hussar_horse_french_trumpet","Light Horse", [("french_hussards_trumpeter_horse",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(45)|horse_maneuver(50)|horse_charge(19)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["lancer_horse_french","Light Horse", [("french_lancier_polonais_horse",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(41)|horse_maneuver(41)|horse_charge(17)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["lancer_horse_french_trumpet","Light Horse", [("french_lancier_polonais_horse_trumpeter",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(41)|horse_maneuver(41)|horse_charge(17)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["dragoon_horse_french","Medium Horse", [("heima",0)], itp_merchandise|itp_type_horse, 0, 500,abundance(90)|hit_points(100)|body_armor(8)|difficulty(3)|horse_speed(40)|horse_maneuver(40)|horse_charge(24)|horse_scale(90),imodbits_horse_basic|imodbit_champion], #patch1115 fix 33/12
 ["dragoon_horse_french_trumpet","Medium Horse", [("french_dragoon_horse_trumpeter",0)], itp_merchandise|itp_type_horse, 0, 500,abundance(90)|hit_points(100)|body_armor(8)|difficulty(3)|horse_speed(40)|horse_maneuver(40)|horse_charge(24)|horse_scale(106),imodbits_horse_basic|imodbit_champion], #patch1115 fix 33/11
 ["cuirassier_horse_french","Heavy Horse", [("hongma",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(115)|body_armor(12)|difficulty(3)|horse_speed(38)|horse_maneuver(39)|horse_charge(32)|horse_scale(90),imodbits_horse_basic|imodbit_champion], #patch1115 fix 33/13
 ["cuirassier_horse_french_officer","Heavy Horse", [("french_cuirassier_officer_horse",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(115)|body_armor(12)|difficulty(3)|horse_speed(38)|horse_maneuver(39)|horse_charge(32)|horse_scale(108),imodbits_horse_basic|imodbit_champion], #patch1115 fix 33/14
 ["cuirassier_horse_french_trumpet","Takeda Horse", [("hongma",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(115)|body_armor(12)|difficulty(3)|horse_speed(38)|horse_maneuver(39)|horse_charge(32)|horse_scale(108),imodbits_horse_basic|imodbit_champion], #patch1115 fix 33/15
 ["carabineer_horse_french","Heavy Horse", [("french_carabineer_horse",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(115)|body_armor(12)|difficulty(3)|horse_speed(38)|horse_maneuver(39)|horse_charge(32)|horse_scale(108),imodbits_horse_basic|imodbit_champion], #patch1115 fix 33/16
 ["carabineer_horse_french_officer","Heavy Horse", [("limaoma",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(115)|body_armor(12)|difficulty(3)|horse_speed(38)|horse_maneuver(39)|horse_charge(32)|horse_scale(108),imodbits_horse_basic|imodbit_champion], #patch1115 fix 33/17
 ["carabineer_horse_french_trumpet","Heavy Horse", [("french_carabineer_trumpeter_horse",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(115)|body_armor(12)|difficulty(3)|horse_speed(38)|horse_maneuver(39)|horse_charge(32)|horse_scale(108),imodbits_horse_basic|imodbit_champion], #patch1115 fix 33/18
 ["heavy_horse_french","Heavy Horse", [("french_grenadier_a_cheval_horse",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(115)|body_armor(12)|difficulty(3)|horse_speed(38)|horse_maneuver(39)|horse_charge(32)|horse_scale(108),imodbits_horse_basic|imodbit_champion], #patch1115 fix 33/19
 ["heavy_horse_french_trumpet","Heavy Horse", [("french_grenadier_a_cheval_horse_trumpeter",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(115)|body_armor(12)|difficulty(3)|horse_speed(38)|horse_maneuver(39)|horse_charge(32)|horse_scale(108),imodbits_horse_basic|imodbit_champion], #patch1115 fix 33/20
 #British
 ["lightdragoon_horse_britain_1","Light Horse", [("baima",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(41)|horse_maneuver(41)|horse_charge(17)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["lightdragoon_horse_britain_2","Light Horse", [("baima",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(41)|horse_maneuver(41)|horse_charge(17)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["lightdragoon_horse_britain_3","Light Horse", [("baima",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(41)|horse_maneuver(41)|horse_charge(17)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["lightdragoon_horse_britain_4","Light Horse", [("baima",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(41)|horse_maneuver(41)|horse_charge(17)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["kgl_horse_britain","Ming light hourse", [("hongma",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(45)|horse_maneuver(50)|horse_charge(19)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["heavydragoon_horse_britain","Heavy Horse", [("british_iniskilling_horse",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(115)|body_armor(12)|difficulty(3)|horse_speed(38)|horse_maneuver(39)|horse_charge(32)|horse_scale(108),imodbits_horse_basic|imodbit_champion], #patch1115 fix 33/10
 ["heavy_horse_britain","Ming_Warhorse", [("huangma",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(115)|body_armor(10)|difficulty(3)|horse_speed(38)|horse_maneuver(39)|horse_charge(32)|horse_scale(108),imodbits_horse_basic|imodbit_champion], #patch1115 fix 33/9
 #Prussian
 ["lancer_horse_prussia_1","Light Horse", [("prussian_cuirassier_horse1",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(41)|horse_maneuver(41)|horse_charge(17)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["lancer_horse_prussia_2","Light Horse", [("prussian_cuirassier_horse2",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(41)|horse_maneuver(41)|horse_charge(17)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["hussar_horse_prussia_1","Light Horse", [("prussian_cuirassier_horse1",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(45)|horse_maneuver(50)|horse_charge(19)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["hussar_horse_prussia_2","Light Horse", [("prussian_cuirassier_horse2",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(45)|horse_maneuver(50)|horse_charge(19)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["dragoon_horse_prussia_1","Medium Horse", [("prussian_dragoon_horse",0)], itp_merchandise|itp_type_horse, 0, 500,abundance(90)|hit_points(100)|body_armor(8)|difficulty(3)|horse_speed(40)|horse_maneuver(40)|horse_charge(24)|horse_scale(106),imodbits_horse_basic|imodbit_champion], #patch1115 fix 33/8
 ["dragoon_horse_prussia_2","Medium Horse", [("prussian_dragoon_horse_trumpeter",0)], itp_merchandise|itp_type_horse, 0, 500,abundance(90)|hit_points(100)|body_armor(8)|difficulty(3)|horse_speed(40)|horse_maneuver(40)|horse_charge(24)|horse_scale(106),imodbits_horse_basic|imodbit_champion], #patch1115 fix 33/7
 ["heavy_horse_prussia_1","Heavy Horse", [("prussian_cuirassier_horse1",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(115)|body_armor(12)|difficulty(3)|horse_speed(38)|horse_maneuver(39)|horse_charge(32)|horse_scale(108),imodbits_horse_basic|imodbit_champion], #patch1115 fix 33/6
 ["heavy_horse_prussia_2","Heavy Horse", [("prussian_cuirassier_horse2",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(115)|body_armor(12)|difficulty(3)|horse_speed(38)|horse_maneuver(39)|horse_charge(32)|horse_scale(108),imodbits_horse_basic|imodbit_champion], #patch1115 fix 33/5
 ["habsburg_light_horse","Habsburg light horse", [("h_scarlet_a1",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(115)|body_armor(14)|difficulty(3)|horse_speed(45)|horse_maneuver(39)|horse_charge(32)|horse_scale(108),imodbits_horse_basic|imodbit_champion],
 ["barded_france","Armored Horse", [("WPlatedCharger2",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(125)|body_armor(20)|difficulty(3)|horse_speed(35)|horse_maneuver(39)|horse_charge(39)|horse_scale(108),imodbits_horse_basic|imodbit_champion],
 ["black_shirt_horse","Medium Horse", [("h_scarlet_a",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(100)|body_armor(12)|difficulty(3)|horse_speed(38)|horse_maneuver(39)|horse_charge(32)|horse_scale(108),imodbits_horse_basic|imodbit_champion],
 #Russian
 ["cossack_horse_russia_1","Qing heavy Horse", [("qing_horse",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(60)|body_armor(26)|hit_points(115)|difficulty(3)|horse_speed(37)|horse_maneuver(39)|horse_charge(33)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["cossack_horse_russia_2","Light Horse", [("russian_cossack_horse2",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(41)|horse_maneuver(41)|horse_charge(17)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["cossack_horse_russia_3","Light Horse", [("russian_cossack_horse3",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(41)|horse_maneuver(41)|horse_charge(17)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["cossack_horse_russia_4","Light Horse", [("russian_cossack_horse4",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(41)|horse_maneuver(41)|horse_charge(17)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["lancer_horse_russia","Light Horse", [("qing_horse2",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(41)|horse_maneuver(41)|horse_charge(17)|horse_scale(106),imodbits_horse_basic|imodbit_champion],
 ["hussar_horse_russia","Light Horse", [("qing_horse3",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(45)|horse_maneuver(50)|horse_charge(19)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["dragoon_horse_russia","Medium Horse", [("qing_horse3",0)], itp_merchandise|itp_type_horse, 0, 500,abundance(90)|hit_points(100)|body_armor(8)|difficulty(3)|horse_speed(40)|horse_maneuver(40)|horse_charge(24)|horse_scale(106),imodbits_horse_basic|imodbit_champion], #patch1115 fix 33/4
 ["heavy_horse_russia","Heavy Horse", [("russian_chevalier_guard_horse",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(115)|body_armor(12)|difficulty(3)|horse_speed(38)|horse_maneuver(39)|horse_charge(32)|horse_scale(108),imodbits_horse_basic|imodbit_champion], #patch1115 fix 33/3

 
 
 #Austrian
 ["lancer_horse_austria","Light Horse", [("austrian_lancer_horse",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(41)|horse_maneuver(41)|horse_charge(17)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["hussar_horse_austria","Light Horse", [("sedlo_konik",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(48)|horse_maneuver(50)|horse_charge(19)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["lightcav_horse_austria","Light Horse", [("selo_konik",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(41)|horse_maneuver(41)|horse_charge(17)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["dragoon_horse_austria","Medium Horse", [("rich_konik",0)], itp_merchandise|itp_type_horse, 0, 500,abundance(90)|hit_points(100)|body_armor(8)|difficulty(3)|horse_speed(40)|horse_maneuver(40)|horse_charge(24)|horse_scale(106),imodbits_horse_basic|imodbit_champion], #patch1115 fix 33/2
 ["heavy_horse_austria","Heavy Horse", [("unik_konik",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(115)|body_armor(12)|difficulty(3)|horse_speed(38)|horse_maneuver(39)|horse_charge(32)|horse_scale(108),imodbits_horse_basic|imodbit_champion], #patch1115 fix 33/1

 #Rhine
 ["lancer_horse_rhine","Light Horse", [("saxon_ulan_horse",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(41)|horse_maneuver(41)|horse_charge(17)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["lancer_horse_rhine_officer","Light Horse", [("saxon_ulan_horse_white",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(41)|horse_maneuver(41)|horse_charge(17)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["hussar_horse_rhine","Light Horse", [("nassau_horse",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(45)|horse_maneuver(50)|horse_charge(19)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["hussar_horse_rhine_officer","Light Horse", [("nassau_horse_off",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(45)|horse_maneuver(50)|horse_charge(19)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["lightcav_horse_rhine","Light Horse", [("baden_dragoon_horse",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(41)|horse_maneuver(41)|horse_charge(17)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["cuirassier_horse_rhine","Heavy Horse", [("westphalian_cuirassier_horse",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(115)|body_armor(12)|difficulty(3)|horse_speed(38)|horse_maneuver(39)|horse_charge(32)|horse_scale(108),imodbits_horse_basic|imodbit_champion], #patch1115 fix 33/13
 ["cuirassier_horse_rhine_officer","Heavy Horse", [("westphalian_cuirassier_horse_off",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(115)|body_armor(12)|difficulty(3)|horse_speed(38)|horse_maneuver(39)|horse_charge(32)|horse_scale(108),imodbits_horse_basic|imodbit_champion], #patch1115 fix 33/14
 ["garde_du_corps_horse_rhine","Heavy Horse", [("garde_du_corps_horse_rank",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(115)|body_armor(12)|difficulty(3)|horse_speed(38)|horse_maneuver(39)|horse_charge(32)|horse_scale(108),imodbits_horse_basic|imodbit_champion], #patch1115 fix 33/13
 ["garde_du_corps_horse_rhine_officer","Heavy Horse", [("garde_du_corps_horse_off",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(115)|body_armor(12)|difficulty(3)|horse_speed(38)|horse_maneuver(39)|horse_charge(32)|horse_scale(108),imodbits_horse_basic|imodbit_champion], #patch1115 fix 33/14
 ["ming_spear3",         "Ming war spear", [("Txz_slq",0)], itp_type_polearm|itp_offset_lance|itp_merchandise| itp_primary|itp_two_handed|itp_wooden_parry|itp_is_pike|itp_no_blur, itc_spear|itcf_carry_spear,
  80 , weight(2.25)|difficulty(0)|spd_rtng(98) | weapon_length(200)|swing_damage(26 , blunt) | thrust_damage(36 ,  pierce),imodbits_polearm ],
  
 ["light_grassland_horse","light Horse", [("Arabs_horse_d",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(80)|body_armor(6)|difficulty(3)|horse_speed(45)|horse_maneuver(45)|horse_charge(35)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
  
 ["dragon_cavalry_horse","Dragon cavalry horse", [("copy_w_horseaa",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(100)|body_armor(5)|difficulty(3)|horse_speed(48)|horse_maneuver(45)|horse_charge(35)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 
 ["mamluk_horse","Armored horse", [("warhorse_sarranid",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(120)|body_armor(20)|difficulty(3)|horse_speed(38)|horse_maneuver(45)|horse_charge(35)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 
 ["sipahi_horse","Armored horse", [("kher_warhorse",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(120)|body_armor(30)|difficulty(3)|horse_speed(38)|horse_maneuver(45)|horse_charge(35)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 
 ["camel","camel", [("camel",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(150)|body_armor(30)|difficulty(3)|horse_speed(30)|horse_maneuver(45)|horse_charge(35)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 #Placeholder horses
 ["lancer_horse_placeholder","Light Horse", [("austrian_hussard_horse",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(41)|horse_maneuver(41)|horse_charge(17)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["hussar_horse_placeholder","Light Horse", [("austrian_hussard_horse",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(3)|horse_speed(45)|horse_maneuver(50)|horse_charge(19)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["dragoon_horse_placeholder","Medium Horse", [("austrian_hussard_horse",0)], itp_merchandise|itp_type_horse, 0, 500,abundance(90)|hit_points(100)|body_armor(8)|difficulty(3)|horse_speed(40)|horse_maneuver(39)|horse_charge(24)|horse_scale(106),imodbits_horse_basic|imodbit_champion],
 ["heavy_horse_placeholder","Heavy Horse", [("austrian_hussard_horse",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(115)|body_armor(12)|difficulty(3)|horse_speed(38)|horse_maneuver(37)|horse_charge(32)|horse_scale(108),imodbits_horse_basic|imodbit_champion],

["tanto_1", "Tanto", [("gekokujo_tanto_1", 0), ("gekokujo_tanto_1_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_no_parry|itp_merchandise|itp_primary|itp_secondary, itcf_thrust_onehanded|itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_show_holster_when_drawn|itcf_carry_dagger_front_left, 
116, weight(0.5)|weapon_length(37)|difficulty(0)|spd_rtng(115)|abundance(100)|swing_damage(19, cut)|thrust_damage(17, pierce), imodbits_sword_high, [] ],

#手雷
#Grenade
["bomb_small", "Small_Bombs", [("bomb", 0)], itp_type_thrown|itp_primary, 65536, 1, weight(15.000000)|abundance(100)|difficulty(0)|accuracy(0)|spd_rtng(45)|shoot_speed(10)|max_ammo(1)|thrust_damage(1, blunt)|weapon_length(8), imodbit_cracked|imodbit_bent|imodbit_battered, []],
   
["bomb_small_ignited", "Small_Bombs", [("bomb2", 0)], itp_no_pick_up_from_ground|itp_type_thrown|itp_primary, 65536, 1, weight(15.000000)|abundance(100)|difficulty(0)|accuracy(0)|spd_rtng(45)|shoot_speed(10)|max_ammo(1)|thrust_damage(1, blunt)|weapon_length(8), imodbit_cracked|imodbit_bent|imodbit_battered, 
[
    (ti_on_init_item, [
        (set_position_delta, 3, 7, 3),
        (particle_system_add_new, "psys_grenade_fire"),
        (particle_system_add_new, "psys_grenade_tail"),
    ]),
  (ti_on_missile_hit,
  [
    (this_or_next|multiplayer_is_server),
    (neg|game_in_multiplayer_mode),
    (store_trigger_param_1, ":thrower_agent"),
    #pos1 - Missile hit position
    (copy_position,pos47,pos1),
    (call_script,"script_explosion_at_position",":thrower_agent",500,250), # Input: shooter_agent_no, max_damage points, range in cm
   ])   ]],
   
 # ["ming_saber","Ming Saber", [("DaMing_yaodao",0),("DaMing_yaodao_scabbard",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
# 210 , weight(1.5)|difficulty(0)|spd_rtng(92) | weapon_length(96)|swing_damage(32 , cut) | thrust_damage(29 ,  pierce),imodbits_sword_high ],
   
["turkish_bomb", "turkish_bomb", [("bomb", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword, 
210 , weight(1.5)|difficulty(0)|spd_rtng(40) | weapon_length(10)|swing_damage(1 , cut) | thrust_damage(1 ,  pierce),imodbits_sword_high, [
  (ti_on_weapon_attack,
  [
    (this_or_next|multiplayer_is_server),
    (neg|game_in_multiplayer_mode),
    (store_trigger_param_1, ":thrower_agent"),
    (agent_get_position, pos47, ":thrower_agent"),
    (call_script,"script_explosion_at_position",":thrower_agent",500,250),
   ])]],
 #Cheat
 ["admin_horse","Admin Cat", [("Cat_adm_horse",0)], itp_type_horse, 0, 600,abundance(100)|hit_points(100)|body_armor(500)|difficulty(0)|horse_speed(400)|horse_maneuver(100)|horse_charge(50)|horse_scale(120),imodbit_spirited],
 ["admin_lancer_horse","Light Horse", [("austrian_hussard_horse",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(0)|horse_speed(41)|horse_maneuver(41)|horse_charge(17)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["admin_hussar_horse","Light Horse", [("austrian_hussard_horse",0)], itp_merchandise|itp_type_horse, 0, 400,abundance(70)|body_armor(6)|hit_points(80)|difficulty(0)|horse_speed(45)|horse_maneuver(50)|horse_charge(19)|horse_scale(104),imodbits_horse_basic|imodbit_champion],
 ["admin_dragoon_horse","Medium Horse", [("austrian_hussard_horse",0)], itp_merchandise|itp_type_horse, 0, 500,abundance(90)|hit_points(100)|body_armor(8)|difficulty(0)|horse_speed(40)|horse_maneuver(39)|horse_charge(24)|horse_scale(106),imodbits_horse_basic|imodbit_champion],
 ["admin_heavy_horse","Heavy Horse", [("austrian_hussard_horse",0)], itp_merchandise|itp_type_horse, 0, 600,abundance(60)|hit_points(115)|body_armor(12)|difficulty(0)|horse_speed(38)|horse_maneuver(37)|horse_charge(32)|horse_scale(108),imodbits_horse_basic|imodbit_champion],

["wakizashi_6", "Bizen_Wakizashi", [("ggekokujo_wakizashi_2", 0), ("ggekokujo_wakizashi_2_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary, itcf_thrust_onehanded|itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_parry_forward_onehanded|itcf_parry_up_onehanded|itcf_parry_right_onehanded|itcf_parry_left_onehanded|itcf_show_holster_when_drawn|itcf_carry_wakizashi, 
482, weight(1.25)|weapon_length(59)|difficulty(0)|spd_rtng(115)|abundance(85)|swing_damage(28, cut)|thrust_damage(19, pierce), imodbits_sword_high, [] ],

["kunai", "kunai", [("gf_kunai_throw", 0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger,
482, weight(3)|weapon_length(30)|difficulty(0)|spd_rtng(115)|abundance(85)|swing_damage(25, cut)|thrust_damage(16, pierce), imodbits_sword_high, [] ],

["russian_chopper2","Russian saber", [("polyak_sablya_b",0),("polyak_sablya_b_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary, itc_longsword|itcf_carry_sword_left_hip|itcf_show_holster_when_drawn, 
210 , weight(1.2)|difficulty(0)|spd_rtng(92) | weapon_length(95)|swing_damage(35 , cut) | thrust_damage(30 ,  pierce),imodbits_sword_high ],

 #Artillery Horses
 #With cannon
 ["arty_horse_cannon_french","Artillery Horse", [("huangma",0)], itp_merchandise|itp_type_horse|itp_is_carriage, 0, 600,abundance(60)|hit_points(200)|body_armor(10)|difficulty(1)|horse_speed(22)|horse_maneuver(10)|horse_charge(21)|horse_scale(116),imodbits_horse_basic|imodbit_champion],
 ["arty_horse_cannon_british","Artillery Horse", [("huangma",0)], itp_merchandise|itp_type_horse|itp_is_carriage, 0, 600,abundance(60)|hit_points(200)|body_armor(10)|difficulty(1)|horse_speed(22)|horse_maneuver(10)|horse_charge(21)|horse_scale(116),imodbits_horse_basic|imodbit_champion],
 ["arty_horse_cannon_russian","Artillery Horse", [("huangma",0)], itp_merchandise|itp_type_horse|itp_is_carriage, 0, 600,abundance(60)|hit_points(200)|body_armor(10)|difficulty(1)|horse_speed(22)|horse_maneuver(10)|horse_charge(21)|horse_scale(116),imodbits_horse_basic|imodbit_champion],
 ["arty_horse_cannon_austrian","Artillery Horse", [("h_scarlet_a1",0)], itp_merchandise|itp_type_horse|itp_is_carriage, 0, 600,abundance(60)|hit_points(200)|body_armor(10)|difficulty(1)|horse_speed(22)|horse_maneuver(10)|horse_charge(21)|horse_scale(116),imodbits_horse_basic|imodbit_champion],
 ["arty_horse_cannon_prussian","Artillery Horse", [("h_scarlet_a1",0)], itp_merchandise|itp_type_horse|itp_is_carriage, 0, 600,abundance(60)|hit_points(200)|body_armor(10)|difficulty(1)|horse_speed(22)|horse_maneuver(10)|horse_charge(21)|horse_scale(116),imodbits_horse_basic|imodbit_champion],
 #With howitzer
 ["arty_horse_howitzer_french","Artillery Horse", [("huangma",0)], itp_merchandise|itp_type_horse|itp_is_carriage, 0, 600,abundance(60)|hit_points(200)|body_armor(10)|difficulty(1)|horse_speed(22)|horse_maneuver(10)|horse_charge(21)|horse_scale(116),imodbits_horse_basic|imodbit_champion],
 ["arty_horse_howitzer_british","Artillery Horse", [("huangma",0)], itp_merchandise|itp_type_horse|itp_is_carriage, 0, 600,abundance(60)|hit_points(200)|body_armor(10)|difficulty(1)|horse_speed(22)|horse_maneuver(10)|horse_charge(21)|horse_scale(116),imodbits_horse_basic|imodbit_champion],
 ["arty_horse_howitzer_russian","Artillery Horse", [("huangma",0)], itp_merchandise|itp_type_horse|itp_is_carriage, 0, 600,abundance(60)|hit_points(200)|body_armor(10)|difficulty(1)|horse_speed(22)|horse_maneuver(10)|horse_charge(21)|horse_scale(116),imodbits_horse_basic|imodbit_champion],
 ["arty_horse_howitzer_austrian","Artillery Horse", [("h_scarlet_a1",0)], itp_merchandise|itp_type_horse|itp_is_carriage, 0, 600,abundance(60)|hit_points(200)|body_armor(10)|difficulty(1)|horse_speed(22)|horse_maneuver(10)|horse_charge(21)|horse_scale(116),imodbits_horse_basic|imodbit_champion],
 ["arty_horse_howitzer_prussian","Artillery Horse", [("h_scarlet_a1",0)], itp_merchandise|itp_type_horse|itp_is_carriage, 0, 600,abundance(60)|hit_points(200)|body_armor(10)|difficulty(1)|horse_speed(22)|horse_maneuver(10)|horse_charge(21)|horse_scale(116),imodbits_horse_basic|imodbit_champion],
 
####################
##  MM ITEMS End  ##
####################



 # Bow and Crossbow
["ming_bow", "Ming Bow", [("DaMing_bow",0),("DaMing_bow_case",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
683 , weight(1.25)|difficulty(0)|spd_rtng(65) | shoot_speed(80) | thrust_damage(20 ,cut),imodbits_none,[]],

["qing_bow1", "Qing Bow", [("qinggong",0),("qinggong_case",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
683 , weight(1.25)|difficulty(0)|spd_rtng(70) | shoot_speed(70) | thrust_damage(26 ,cut),imodbits_none,[]],

["qing_bow2", "Qing Bow", [("qinggong2",0),("qinggong2_case",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
683 , weight(1.25)|difficulty(0)|spd_rtng(70) | shoot_speed(70) | thrust_damage(26 ,cut),imodbits_none,[]],

["qing_bow3", "Qing Bow", [("qinggong3",0),("qinggong3_case",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
683 , weight(1.25)|difficulty(0)|spd_rtng(70) | shoot_speed(70) | thrust_damage(26 ,cut),imodbits_none,[]],

["qing_bow4", "Qing Bow", [("qinggong4",0),("qinggong3_case",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
683 , weight(1.25)|difficulty(0)|spd_rtng(70) | shoot_speed(70) | thrust_damage(26 ,cut),imodbits_none,[]],

["ming_crossbow", "Ming crossbow", [("crossbow_shenbi",0)], itp_type_crossbow |itp_primary|itp_two_handed|itp_cant_reload_on_horseback ,itcf_shoot_musket|itcf_reload_musket|itcf_carry_crossbow_back, 
683 , weight(3.75)|difficulty(0)|spd_rtng(35)|  shoot_speed(70) | thrust_damage(50,cut)|max_ammo(1),imodbits_crossbow ],

["yumi_8", "War_Yumi", [("gekokujo_yumi_8", 0), ("gekokujo_yumi_8_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 
862, weight(1.75)|difficulty(0)|spd_rtng(61)|shoot_speed(55)|abundance(100)|thrust_damage(24, cut)|max_ammo(0), imodbits_bow, [] ],

["yumi_9", "War_Yumi", [("gekokujo_yumi_7", 0), ("gekokujo_yumi_7_carry", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bow_back, 
862, weight(1.75)|difficulty(0)|spd_rtng(61)|shoot_speed(55)|abundance(100)|thrust_damage(24, cut)|max_ammo(0), imodbits_bow, [] ],


["turkish_bow", "saracin_bow_a", [("saracin_bow_a", 0), ("saracin_bow_case_a", ixmesh_carry)], itp_type_bow|itp_merchandise|itp_two_handed|itp_primary, itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
862, weight(1.75)|difficulty(0)|spd_rtng(61)|shoot_speed(42)|abundance(100)|thrust_damage(26, cut)|max_ammo(0), imodbits_bow, [] ],

["russian_bow", "Russian bow", [("dedal_bow_tatar_c", 0), ("dedal_bowcase_tatar_c", ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
862, weight(1.75)|difficulty(0)|spd_rtng(61)|shoot_speed(42)|abundance(100)|thrust_damage(26, cut)|max_ammo(0), imodbits_bow, [] ],

["qing_bow_ai", "Qing Bow", [("qinggong",0),("qinggong_case",ixmesh_carry)], itp_type_bow |itp_merchandise|itp_primary|itp_two_handed ,itcf_shoot_bow|itcf_carry_bowcase_left|itcf_show_holster_when_drawn, 
683 , weight(1.25)|difficulty(0)|spd_rtng(70) | shoot_speed(70) | thrust_damage(16 ,cut),imodbits_none,[]],


 # Arrows
["ming_arrows","Ming_Arrows", [("DaMing_arrow",0),("DaMing_arrow",ixmesh_flying_ammo),("DaMing_quiver", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
683 , weight(3.0)|weapon_length(91)|thrust_damage(35,cut)|max_ammo(23),imodbits_none,[]],

["qing_arrows","Qing_Arrows", [("DaMing_arrow",0),("DaMing_arrow",ixmesh_flying_ammo),("arrows_a_kolchan_I", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
683 , weight(3.0)|weapon_length(91)|thrust_damage(40,cut)|max_ammo(23),imodbits_none,[]],

["qing_arrows_fire","Qing_Arrows(Fire)", [("amazon_arrow",0),("firearrow",ixmesh_flying_ammo),("amazon_quiver_new", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
683 , weight(3.0)|weapon_length(91)|thrust_damage(50,cut)|max_ammo(18),imodbits_none,[]], 


["turkish_arrow","turkish_arrow", [("dedal_arrow_tatar_c",0),("dedal_arrow_tatar_c_fly",ixmesh_flying_ammo),("dedal_kolczan_tatar_c", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
683 , weight(3.0)|weapon_length(91)|thrust_damage(35,cut)|max_ammo(23),imodbits_none,[]],

["russian_arrow","Russian arrow", [("dedal_arrow_tatar_c",0),("dedal_arrow_tatar_c_fly",ixmesh_flying_ammo),("dedal_kolczan_tatar_c", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
683 , weight(2.0)|weapon_length(110)|thrust_damage(35,cut)|max_ammo(25),imodbits_none,[]],

["rocketarrows_dummy", "{!}rocketarrows_dummy", [("Russian_gusarskiy_karabin",0)], itp_type_crossbow |itp_merchandise|itp_primary|itp_two_handed|custom_kill_info(2),itcf_shoot_musket|itcf_carry_crossbow_back, 
683 , weight(3.0)|difficulty(0)|spd_rtng(150) | shoot_speed(40) | thrust_damage(80 ,pierce)|max_ammo(100)|accuracy(75),imodbits_none,
 []],

["jap_arrows2", "War_Arrows", [("gf_arrow_3", 0), ("gf_arrow_3_flying", ixmesh_flying_ammo), ("gf_quiver_3", ixmesh_carry)], itp_type_arrows|itp_merchandise, itcf_carry_quiver_back_right, 
410, weight(3)|weapon_length(95)|abundance(50)|thrust_damage(35,cut)|max_ammo(23), imodbits_missile, [] ],

["bolts","Blots", [("cartridge_box_mesh",0),("bullet_projectile",ixmesh_flying_ammo),("cartridge_a",ixmesh_carry)], itp_type_bolts|itp_merchandise|itp_default_ammo|itp_can_penetrate_shield, 0, 64,weight(2.0)|abundance(100)|weapon_length(1)|thrust_damage(1,pierce)|max_ammo(18),imodbits_missile,
 [(ti_on_missile_hit, [(copy_position,pos63,pos1),(store_trigger_param_2, ":collision_type"),(call_script, "script_mm_on_bullet_hit",":collision_type")])]],

["rocketarrows","huojian", [("amazon_arrow",0),("firearrow",ixmesh_flying_ammo)], itp_type_bolts|itp_merchandise|itp_can_penetrate_shield, 0, 64,weight(2.0)|abundance(100)|weapon_length(1)|thrust_damage(100,pierce)|max_ammo(1),imodbits_missile, [
    (ti_on_missile_hit, [
        (try_begin),
            (multiplayer_is_server),
            (store_trigger_param_1, ":var_0"),
            (set_position_delta, 500, 600, 500),
            (particle_system_burst, 10, pos1, 100),
        (try_end),
    ]),
]], 



["items_end", "Items End", [("empty_mesh",0)], 0, 0, 1, 0, 0],
]



