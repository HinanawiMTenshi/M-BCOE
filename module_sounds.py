from header_sounds import *
from ID_factions import *

# default values:
# sf_priority_5
# sf_vol_10

sounds = [
 ("click", sf_2d|sf_vol_7,["click_v15.ogg"]),##ilam y

 ("gong", sf_2d|sf_priority_9|sf_vol_7, []),
 ("quest_taken", sf_2d|sf_priority_9|sf_vol_7, []),
 ("quest_completed", sf_2d|sf_priority_9|sf_vol_7, []),
 ("quest_succeeded", sf_2d|sf_priority_9|sf_vol_7, []),
 ("quest_concluded", sf_2d|sf_priority_9|sf_vol_7, []),
 ("quest_failed", sf_2d|sf_priority_9|sf_vol_7, []),
 ("quest_cancelled", sf_2d|sf_priority_9|sf_vol_7, []),
 ("rain",sf_2d|sf_priority_15|sf_vol_4|sf_looping, ["ambient_sound_new_rain.wav"]),
 ("snow",sf_2d|sf_priority_15|sf_vol_4|sf_looping, ["ambient_sound_new_snow.ogg"]),
 ("money_received",sf_2d|sf_priority_10|sf_vol_6, []),
 ("money_paid",sf_2d|sf_priority_10|sf_vol_10, []),
 ("sword_clash_1", sf_priority_3|sf_vol_10,
 
 [
 "weapon_sound_new_sword_block_1.ogg",
 "weapon_sound_new_sword_block_2.ogg",
 "weapon_sound_new_sword_block_3.ogg",
 "weapon_sound_new_sword_block_4.ogg",
 "weapon_sound_new_sword_block_5.ogg",
 "weapon_sound_new_sword_block_6.ogg",
 "weapon_sound_new_sword_block_7.ogg",
 "weapon_sound_new_sword_block_10.ogg",
 "weapon_sound_new_sword_block_11.ogg",
 "weapon_sound_new_sword_block_12.ogg",
 "weapon_sound_new_sword_block_13.ogg",
 "weapon_sound_new_sword_block_14.ogg",
 "weapon_sound_new_sword_block_15.ogg",
 "weapon_sound_new_sword_block_16.ogg",
 "weapon_sound_new_sword_block_17.ogg",
 "weapon_sound_new_sword_block_18.ogg",
 "weapon_sound_new_sword_block_19.ogg",
 "weapon_sound_new_sword_block_20.ogg"
 
 ]),
 ##ilam
 
 ("sword_clash_2", 0,[]),#"s_swordClash2.wav"]),
 ("sword_clash_3", 0,[]),#"s_swordClash3.wav"]),
 
 ("sword_swing", sf_priority_2|sf_vol_8,["weapon_sound_new_swing.ogg","weapon_swing_01.ogg","weapon_swing_02.ogg","weapon_swing_03.ogg","weapon_swing_04.ogg","weapon_swing_05.ogg"]),##ilam y
 
 ("footstep_grass", sf_priority_1|sf_vol_4,
 ["footstep_1.ogg","footstep_2.ogg","footstep_3.ogg","footstep_4.ogg"]),##ilam
 
 ("footstep_wood", sf_priority_1|sf_vol_6,
 ["footstep_wood_1.wav","footstep_wood_2.wav","footstep_wood_4.wav"]),##ilam

 ("footstep_water", sf_priority_1|sf_vol_3,
 ["water_walk_1.ogg","water_walk_2.ogg","water_walk_3.ogg","water_walk_4.ogg","water_walk_5.ogg"]),##ilam
 
 ("footstep_horse",sf_priority_8|sf_vol_8, []),#"footstep_horse_5.ogg","footstep_horse_2.ogg","footstep_horse_3.ogg","footstep_horse_4.ogg"]),
# ("footstep_horse",0, ["s_footstep_horse_4b.wav","s_footstep_horse_4f.wav","s_footstep_horse_5b.wav","s_footstep_horse_5f.wav"]),
 ("footstep_horse_1b",sf_priority_8|sf_vol_8, ["s_footstep_horse_4b.wav","s_footstep_horse_4f.wav","s_footstep_horse_5b.wav","s_footstep_horse_5f.wav"]),
 ("footstep_horse_1f",sf_priority_8|sf_vol_8, ["s_footstep_horse_2b.wav","s_footstep_horse_2f.wav","s_footstep_horse_3b.wav","s_footstep_horse_3f.wav"]),
# ("footstep_horse_1f",sf_priority_3|sf_vol_15, ["footstep_horse_5.ogg","footstep_horse_2.ogg","footstep_horse_3.ogg","footstep_horse_4.ogg"]),
 ("footstep_horse_2b",sf_priority_8|sf_vol_8, ["s_footstep_horse_2b.wav"]),
 ("footstep_horse_2f",sf_priority_8|sf_vol_8, ["s_footstep_horse_2f.wav"]),
 ("footstep_horse_3b",sf_priority_8|sf_vol_8, ["s_footstep_horse_3b.wav"]),
 ("footstep_horse_3f",sf_priority_8|sf_vol_8, ["s_footstep_horse_3f.wav"]),
 ("footstep_horse_4b",sf_priority_8|sf_vol_8, ["s_footstep_horse_4b.wav"]),
 ("footstep_horse_4f",sf_priority_8|sf_vol_8, ["s_footstep_horse_4f.wav"]),
 ("footstep_horse_5b",sf_priority_8|sf_vol_8, ["s_footstep_horse_5b.wav"]),
 ("footstep_horse_5f",sf_priority_8|sf_vol_8, ["s_footstep_horse_5f.wav"]),
 
 ##ilam
 ("jump_begin", sf_vol_7|sf_priority_9,["jump_new_begin.ogg"]),
 ("jump_end", sf_vol_5|sf_priority_9,["jump_new_end.ogg"]),
 ("jump_begin_water", sf_vol_4|sf_priority_9,
 ["jump_water_begin_new.ogg", "jump_water_begin_new_2.ogg", "jump_water_begin_new_3.ogg", "jump_water_begin_new_4.ogg"]),
 ("jump_end_water", sf_vol_4|sf_priority_9,
 ["jump_water_end_new.ogg", "jump_water_end_new_2.ogg","jump_water_end_new_3.ogg","jump_water_end_new_4.ogg","jump_water_end_new_5.ogg","jump_water_end_new_6.ogg"]),
 ("horse_jump_begin", sf_vol_8|sf_priority_9,["horse_jump_e_new_01.ogg"]),
 ("horse_jump_end", sf_vol_8|sf_priority_9,["horse_jump_e_new_02.ogg"]),
 ("horse_jump_begin_water", sf_vol_6|sf_priority_9,["jump_water_begin_new.ogg"]),
 ("horse_jump_end_water", sf_vol_6|sf_priority_9,["jump_water_end_new.ogg"]),

 ("release_bow",sf_vol_8, ["mms_bow_shoot_01.ogg","bow_shoot_01.ogg","bow_shoot_02.ogg","bow_shoot_03.ogg","bow_shoot_04.ogg","bow_shoot_05.ogg","bow_shoot_06.ogg","bow_shoot_07.ogg","bow_shoot_08.ogg","bow_shoot_09.ogg","bow_shoot_10.ogg"]),
 ("release_crossbow",sf_vol_1, []),
 ("throw_javelin",sf_vol_5, ["throw_javelin_2.ogg"]),
 ("throw_axe",sf_vol_5, ["throw_javelin_01.ogg","throw_javelin_02.ogg","throw_javelin_03.ogg"]),
 ("throw_knife",sf_vol_5, ["throw_knife_01.ogg","throw_knife_02.ogg","throw_knife_03.ogg","throw_knife_04.ogg"]),
 ("throw_stone",sf_vol_7, ["throw_stone_1.wav"]),

 ("reload_crossbow",sf_priority_1|sf_vol_2, ["missile_reload_musket_new.wav"]),##ilam
 ("reload_crossbow_continue",sf_priority_3|sf_vol_2, []),
 ("pull_bow",sf_vol_6, ["pull_bow_1.ogg","pull_bow_string_01.ogg","pull_bow_string_02.ogg","pull_bow_string_03.ogg","pull_bow_string_04.ogg","pull_bow_string_05.ogg"]),
 ("pull_arrow",sf_vol_5, ["draw_arrow_01.ogg","draw_arrow_02.ogg","draw_arrow_03.ogg"]),
 
 ("bolt_pass_by",0, 
 [
 "missile_pass_new_01.ogg",
 "missile_pass_new_02.ogg",
 "missile_pass_new_03.ogg",
 "missile_pass_new_04.ogg",
 "missile_pass_new_05.ogg",
 "missile_pass_new_06.ogg",
 "missile_pass_new_07.ogg",
 "missile_pass_new_08.ogg",
 "missile_pass_new_09.ogg",
 "missile_pass_new_10.ogg",
 "missile_pass_new_11.ogg",
 "missile_pass_new_12.ogg"
 
 ]), ##ilam
 
 ("javelin_pass_by",0, ["javelin_pass_by_1.ogg","javelin_pass_by_2.ogg"]),
 ("stone_pass_by",sf_vol_9, ["stone_pass_01.ogg","stone_pass_02.ogg","stone_pass_03.ogg"]),
 ("axe_pass_by",0, ["axe_pass_by_1.ogg"]),
 ("knife_pass_by",0, ["knife_pass_01.ogg","knife_pass_02.ogg","knife_pass_03.ogg","knife_pass_04.ogg"]),
 
 ("bullet_pass_by",0, 
 [ "missile_pass_new_01.ogg",
 "missile_pass_new_02.ogg",
 "missile_pass_new_03.ogg",
 "missile_pass_new_04.ogg",
 "missile_pass_new_05.ogg",
 "missile_pass_new_06.ogg",
 "missile_pass_new_07.ogg",
 "missile_pass_new_08.ogg",
 "missile_pass_new_09.ogg",
 "missile_pass_new_10.ogg",
 "missile_pass_new_11.ogg",
 "missile_pass_new_12.ogg"
 ]), ##ilam
 
 ("incoming_arrow_hit_ground",sf_priority_7|sf_vol_7, ["arrow_ground_01.wav","arrow_ground_02.wav","arrow_ground_03.wav","arrow_ground_04.wav","arrow_ground_05.wav","arrow_ground_06.wav","arrow_ground_07.wav","arrow_ground_08.wav",]),
 ("incoming_bolt_hit_ground",sf_priority_7|sf_vol_10, ["missile_hit_ground_new_1.ogg", "missile_hit_ground_new_2.ogg", "missile_hit_ground_new_3.ogg"]), ##ilam
 ("incoming_javelin_hit_ground",sf_priority_7|sf_vol_7, ["javelin_ground_01.ogg","javelin_ground_02.ogg","javelin_ground_03.ogg"]),
 ("incoming_stone_hit_ground",sf_priority_7|sf_vol_7, ["stone_ground_01.ogg","stone_ground_02.ogg","stone_ground_03.ogg"]),
 ("incoming_axe_hit_ground",sf_priority_7|sf_vol_7, ["axe_ground_01.ogg","axe_ground_02.ogg","axe_ground_03.ogg"]),
 ("incoming_knife_hit_ground",sf_priority_7|sf_vol_7, ["knife_ground_01.ogg","knife_ground_02.ogg","knife_ground_03.ogg"]),
 ("incoming_bullet_hit_ground",sf_priority_7|sf_vol_10, ["missile_hit_ground_new_1.ogg", "missile_hit_ground_new_2.ogg", "missile_hit_ground_new_3.ogg"]),

 ("outgoing_arrow_hit_ground",sf_priority_7|sf_vol_7, ["arrow_ground_01.ogg","arrow_ground_02.ogg","arrow_ground_03.ogg","arrow_ground_04.ogg","arrow_ground_05.ogg","arrow_ground_06.ogg","arrow_ground_07.ogg","arrow_ground_08.ogg"]),
 ("outgoing_bolt_hit_ground",sf_priority_7|sf_vol_10,  ["missile_hit_ground_new_1.ogg", "missile_hit_ground_new_2.ogg", "missile_hit_ground_new_3.ogg"]), ##ilam
 ("outgoing_javelin_hit_ground",sf_priority_7|sf_vol_10, ["javelin_ground_01.ogg","javelin_ground_02.ogg","javelin_ground_03.ogg"]),
 ("outgoing_stone_hit_ground",sf_priority_7|sf_vol_7, ["stone_ground_01.ogg","stone_ground_02.ogg","stone_ground_03.ogg"]),
 ("outgoing_axe_hit_ground",sf_priority_7|sf_vol_7, ["axe_ground_01.ogg","axe_ground_02.ogg","axe_ground_03.ogg"]),
 ("outgoing_knife_hit_ground",sf_priority_7|sf_vol_7, ["knife_ground_01.ogg","knife_ground_02.ogg","knife_ground_03.ogg"]),
 ("outgoing_bullet_hit_ground",sf_priority_7|sf_vol_10, ["missile_hit_ground_new_1.ogg", "missile_hit_ground_new_2.ogg", "missile_hit_ground_new_3.ogg"]),##ilam

 ("draw_sword",sf_priority_1|sf_vol_6, 
 ["weapon_sound_new_sword_draw_1.wav",
 "weapon_sound_new_sword_draw_2.wav",
 "weapon_sound_new_sword_draw_3.wav",
 "weapon_sound_new_sword_draw_4.wav",
 "weapon_sound_new_sword_draw_5.wav",
 "weapon_sound_new_sword_draw_6.wav",
 "weapon_sound_new_sword_draw_7.wav",
  "weapon_sound_new_sword_draw_8.wav"
 ]),##ilam
 ("put_back_sword",sf_priority_4, ["put_away_sword_01.ogg"]),
 ("draw_greatsword",sf_priority_4, ["draw_greatsword_01.ogg","draw_greatsword_03.ogg"]),
 ("put_back_greatsword",sf_priority_4, ["put_away_greatsword_01.ogg"]),
 ("draw_axe",sf_priority_1|sf_vol_3, ["draw_mace.wav"]),
 ("put_back_axe",sf_priority_4, ["put_away_axe_01.ogg"]),
 ("draw_greataxe",sf_priority_1|sf_vol_3, ["draw_greataxe.wav"]),
 ("put_back_greataxe",sf_priority_1|sf_vol_3, ["put_back_to_leather.wav"]),
 ("draw_spear",sf_priority_1|sf_vol_3, ["weapon_sound_new_spear.ogg", "weapon_sound_new_spear_2.ogg", "draw_spear_new_01.wav", "draw_spear_new_02.wav"]),
 ("put_back_spear",sf_priority_1|sf_vol_3, ["put_back_to_leather.wav"]),
 ("draw_crossbow",sf_priority_1|sf_vol_3, ["weapon_sound_new_musket.ogg", "draw_shield_new_01.wav", "draw_shield_new_02.wav"]),
 ("put_back_crossbow",sf_priority_1|sf_vol_3, ["put_back_to_leather.wav"]),
 ("draw_revolver",sf_priority_1|sf_vol_3, ["draw_from_holster.wav"]),
 ("put_back_revolver",sf_priority_1|sf_vol_3, ["put_back_to_holster.wav"]),
 ("draw_dagger",sf_priority_4, ["draw_dagger_01.ogg","draw_dagger_02.ogg"]),
 ("put_back_dagger",sf_priority_4, ["put_away_dagger_01.ogg"]),
 ##ilam 
 
 ("draw_bow",sf_priority_1|sf_vol_3, ["draw_bow_01.wav"]),
 ("put_back_bow",sf_priority_1|sf_vol_3, ["put_away_bow_01.wav"]),
 ("draw_shield",sf_priority_2|sf_vol_4, ["draw_shield.ogg"]),
 ("put_back_shield",sf_priority_1|sf_vol_4, ["put_back_shield.ogg"]),
 ("draw_other",sf_priority_1|sf_vol_3, ["draw_other.wav"]),
 ("put_back_other",sf_priority_1|sf_vol_3, ["draw_other2.wav"]),

 ("body_fall_small",sf_priority_6|sf_vol_10, ["body_fall_new_1.wav","body_fall_new_2.wav","body_fall_new_3.wav"]),
 ("body_fall_big",sf_priority_6|sf_vol_10, ["body_fall_new_1.wav","body_fall_new_2.wav","body_fall_new_3.wav"]),
 ("horse_body_fall_begin",sf_priority_6|sf_vol_10, ["horse_body_fall_begin_1_new.wav"]),
 ("horse_body_fall_end",sf_priority_6|sf_vol_10, ["horse_body_fall_end_1_new.wav","body_fall_2.wav"]),
 
 ("hit_wood_wood",sf_priority_6|sf_vol_7, ["hit_wood_wood_1.wav","hit_wood_wood_2.wav","hit_wood_wood_3.wav","hit_wood_wood_4.wav","hit_wood_metal_4.wav","hit_wood_metal_5.wav","hit_wood_metal_6.wav"]),#dummy

 ##ilam
 ("hit_metal_metal",sf_priority_6|sf_vol_7, 
 [                               
 "weapon_sound_new_sword_block_1.ogg",
 "weapon_sound_new_sword_block_2.ogg",
 "weapon_sound_new_sword_block_3.ogg",
 "weapon_sound_new_sword_block_4.ogg",
 "weapon_sound_new_sword_block_5.ogg",
 "weapon_sound_new_sword_block_6.ogg",
 "weapon_sound_new_sword_block_7.ogg",
 "weapon_sound_new_sword_block_10.ogg",
 "weapon_sound_new_sword_block_11.ogg",
 "weapon_sound_new_sword_block_12.ogg",
 "weapon_sound_new_sword_block_13.ogg",
 "weapon_sound_new_sword_block_14.ogg",
 "weapon_sound_new_sword_block_15.ogg",
 "weapon_sound_new_sword_block_16.ogg",
 "weapon_sound_new_sword_block_17.ogg",
 "weapon_sound_new_sword_block_18.ogg",
 "weapon_sound_new_sword_block_19.ogg",
 "weapon_sound_new_sword_block_20.ogg"
 #"Sword_clash_21.ogg",
 #"Sword_clash_22.ogg"
 
 ]),##ilam

 ("hit_wood_metal",sf_priority_6|sf_vol_7, ["hit_metal_metal_1.wav","hit_metal_metal_2.wav","hit_wood_metal_7.wav"
 ,"metal_on_wood_02.ogg", "metal_on_wood_03.ogg", "metal_on_wood_04.ogg"]),##ilam

 ("shield_hit_wood_wood",sf_priority_7|sf_vol_9, ["shield_hit_wood_wood_1.ogg","shield_hit_wood_wood_2.ogg","shield_hit_wood_wood_3.ogg"]),
 ("shield_hit_metal_metal",sf_priority_7|sf_vol_10, ["shield_hit_metal_metal_1.ogg","shield_hit_metal_metal_2.ogg","shield_hit_metal_metal_3.ogg","shield_hit_metal_metal_4.ogg"]),
 ("shield_hit_wood_metal",sf_priority_7|sf_vol_10, ["shield_hit_cut_3.ogg","shield_hit_cut_4.ogg","shield_hit_cut_5.ogg","shield_hit_cut_10.ogg"]), #(shield is wood)
 ("shield_hit_metal_wood",sf_priority_7|sf_vol_10, ["shield_hit_metal_wood_1.ogg","shield_hit_metal_wood_2.ogg","shield_hit_metal_wood_3.ogg"]),#(shield is metal)
 ("shield_broken",sf_priority_9, ["shield_broken.ogg"]),
 ("man_hit",sf_priority_5|sf_vol_7, [
  "man_pain_new_01.wav",
  "man_pain_new_02.wav",
  "man_pain_new_03.wav",
  "man_pain_new_04.wav",
  "man_pain_new_05.wav",
  "man_pain_new_06.wav",
  "man_pain_new_07.wav",
  "man_pain_new_08.wav",
  "man_pain_new_09.wav",
  "man_pain_new_10.wav",
  "man_pain_new_11.wav",
  "man_pain_new_12.wav",
  "man_pain_new_13.wav",
  "man_pain_new_14.wav",
  "man_pain_new_15.wav",
  "man_pain_new_16.wav",
  "man_pain_new_17.wav",
  "man_pain_new_18.wav",
  "man_pain_new_19.wav",
  "man_pain_new_20.wav",
  "man_pain_new_21.wav",
  "man_pain_new_22.wav",
  "man_pain_new_23.wav",
  "man_pain_new_24.wav",
  "man_pain_new_25.wav",
  #new in 15.2
  "man_pain_new_26.wav", 
  "man_pain_new_27.wav", 
  "man_pain_new_28.wav", 
  "man_pain_new_29.wav", 
  "man_pain_new_30.wav", 
  "man_pain_new_31.wav" 

 ]),
 # ("man_hit",sf_priority_5|sf_vol_7, ["man_hit_5.wav","man_hit_6.wav","man_hit_7.wav","man_hit_8.wav","man_hit_9.wav","man_hit_10.wav","man_hit_11.wav","man_hit_12.wav","man_hit_13.wav","man_hit_14.wav","man_hit_15.wav",
                                      # "man_hit_17.wav","man_hit_18.wav","man_hit_19.wav","man_hit_22.wav","man_hit_29.wav","man_hit_32.wav","man_hit_47.wav","man_hit_57.wav","man_hit_59.wav"]),
 
 ("man_die",sf_priority_6|sf_vol_10, [
  "man_die_new_01.wav",
  "man_die_new_02.wav",
  "man_die_new_03.wav",
  "man_die_new_04.wav",
  "man_die_new_05.wav",
  "man_die_new_06.wav",
  "man_die_new_07.wav",
  "man_die_new_08.wav",
  "man_die_new_09.wav",
  "man_die_new_10.wav",#10
  "man_die_new_11.wav",
  "man_die_new_12.wav",
  "man_die_new_13.wav",
  "man_die_new_14.wav",
  "man_die_new_15.wav",
  "man_die_new_16.wav",
  "man_die_new_17.wav",
  "man_die_new_18.wav",
  "man_die_new_19.wav",
  "man_die_new_20.wav",#20
  "man_die_new_21.wav",
  "man_die_new_22.wav",
  "man_die_new_23.wav",
  "man_die_new_24.wav",
  "man_die_new_25.wav",
  "man_die_new_26.wav",
  "man_die_new_27.wav",
  "man_die_new_28.wav",
  "man_die_new_29.wav",
  "man_die_new_30.wav",#30
  "man_die_new_31.wav",
  "man_die_new_32.wav"##MAXIMUM 32



 ]),
 # ("man_die",sf_priority_6|sf_vol_8,  ["man_death_1.wav","man_death_8.wav","man_death_8b.wav","man_death_11.wav","man_death_14.wav","man_death_16.wav","man_death_18.wav","man_death_21.wav","man_death_29.wav","man_death_40.wav","man_death_44.wav","man_death_46.wav","man_death_48.wav","man_death_64.wav"
                            # MM
                             # ,"death1.wav","death2.wav","death3.wav","death4.wav"
                             # ]),# ["man_fall_1.ogg","man_fall_2.ogg","man_fall_3.ogg","man_fall_4.ogg"]),
 ("woman_hit",sf_priority_5|sf_vol_7, [
								"woman_pain_new_01.wav",
								"woman_pain_new_02.wav",
								"woman_pain_new_03.wav",
								"woman_pain_new_04.wav",
								"woman_pain_new_05.wav",
								"woman_pain_new_06.wav",
								"woman_pain_new_07.wav",
								"woman_pain_new_08.wav",
								"woman_pain_new_09.wav",
								"woman_pain_new_10.wav",
								"woman_pain_new_11.wav",
								"woman_pain_new_12.wav",
								"woman_pain_new_13.wav",
								"woman_pain_new_14.wav",
								"woman_pain_new_15.wav",
								"woman_pain_new_16.wav",
								"woman_pain_new_17.wav",
								"woman_pain_new_18.wav",
								"woman_pain_new_19.wav",
								"woman_pain_new_20.wav"

                              ]),
 ("woman_die",sf_priority_6|sf_vol_8, [
	"woman_death_new_01.wav",
	"woman_death_new_02.wav",
	"woman_death_new_03.wav",
	"woman_death_new_04.wav",
	"woman_death_new_05.wav",
	"woman_death_new_06.wav",
	"woman_death_new_07.wav",
	"woman_death_new_08.wav",
	"woman_death_new_09.wav",
	"woman_death_new_10.wav",
	"woman_death_new_11.wav",
	"woman_death_new_12.wav",
	"woman_death_new_13.wav",
	"woman_death_new_14.wav",
	"woman_death_new_15.wav",
	"woman_death_new_16.wav",
	"woman_death_new_17.wav",
	"woman_death_new_18.wav",
	"woman_death_new_19.wav",
	"woman_death_new_20.wav",
	"woman_death_new_21.wav",
	"woman_death_new_22.wav"
 ]),
 ("woman_yell",sf_priority_10|sf_vol_10, []),#"woman_yell_1.wav","woman_yell_2.wav"]),
 ("hide",0, []),
 ("unhide",0, []),
 ("neigh",sf_priority_5|sf_vol_6, ["horse_exterior_whinny_01.wav","horse_exterior_whinny_02.wav","horse_exterior_whinny_03.wav","horse_exterior_whinny_04.wav","horse_exterior_whinny_05.wav","horse_whinny.wav"]),
 ("gallop",sf_priority_8|sf_vol_12, ["horse_gallop_new_01.ogg","horse_gallop_new_04.ogg","horse_gallop_new_03.ogg","horse_gallop_new_02.ogg","horse_gallop_new_05.ogg",]),
 ##ilam gallop
 ("battle",sf_vol_4, []),
 ("arrow_hit_body",sf_priority_5|sf_vol_7, 
 ["missile_flesh_01.ogg","missile_flesh_05.ogg","missile_flesh_07.ogg","missile_flesh_09.ogg"]),
 
("metal_hit_low_armor_low_damage",sf_priority_5|sf_vol_9, ["metal_low_low_01.ogg","metal_low_low_02.ogg","metal_low_low_03.ogg","metal_low_low_04.ogg","metal_low_low_05.ogg","metal_low_low_06.ogg","metal_low_low_07.ogg","metal_low_low_08.ogg"]),
 
 ("metal_hit_low_armor_high_damage",sf_priority_5|sf_vol_9, ["metal_low_high_01.ogg","metal_low_high_02.ogg","metal_low_high_03.ogg","metal_low_high_04.ogg","metal_low_high_05.ogg","metal_low_high_06.ogg","metal_low_high_07.ogg","metal_low_high_08.ogg","metal_low_high_09.ogg","metal_low_high_10.ogg","metal_low_high_11.ogg","metal_low_high_12.ogg","metal_low_high_13.ogg","metal_low_high_14.ogg","metal_low_high_15.ogg","metal_low_high_16.ogg","metal_low_high_17.ogg","metal_low_high_18.ogg","metal_low_high_19.ogg","metal_low_high_20.ogg","metal_low_high_21.ogg","metal_low_high_22.ogg","metal_low_high_23.ogg","metal_low_high_24.ogg","metal_low_high_25.ogg","metal_low_high_26.ogg","metal_low_high_27.ogg"]),
 
 ("metal_hit_high_armor_low_damage",sf_priority_5|sf_vol_9, ["metal_high_low_01.ogg","metal_high_low_02.ogg","metal_high_low_03.ogg","metal_high_low_04.ogg","metal_high_low_05.ogg","metal_high_low_06.ogg","metal_high_low_07.ogg","metal_high_low_08.ogg","metal_high_low_09.ogg","metal_high_low_10.ogg","metal_high_low_11.ogg","metal_high_low_12.ogg","metal_high_low_13.ogg","metal_high_low_14.ogg","metal_high_low_15.ogg","metal_high_low_16.ogg","metal_high_low_17.ogg","metal_high_low_18.ogg","metal_high_low_19.ogg","metal_high_low_20.ogg","metal_high_low_21.ogg","metal_high_low_22.ogg","metal_high_low_23.ogg","metal_high_low_24.ogg","metal_high_low_25.ogg"]),
 
 ("metal_hit_high_armor_high_damage",sf_priority_5|sf_vol_9, ["metal_high_high_01.ogg","metal_high_high_02.ogg","metal_high_high_03.ogg","metal_high_high_04.ogg","metal_high_high_05.ogg","metal_high_high_06.ogg","metal_high_high_07.ogg","metal_high_high_08.ogg","metal_high_high_09.ogg","metal_high_high_10.ogg","metal_high_high_11.ogg","metal_high_high_12.ogg","metal_high_high_13.ogg","metal_high_high_14.ogg","metal_high_high_15.ogg","metal_high_high_16.ogg","metal_high_high_17.ogg","metal_high_high_18.ogg","metal_high_high_19.ogg","metal_high_high_20.ogg","metal_high_high_21.ogg","metal_high_high_22.ogg","metal_high_high_23.ogg","metal_high_high_24.ogg","metal_high_high_25.ogg","metal_high_high_26.ogg","metal_high_high_27.ogg","metal_high_high_28.ogg","metal_high_high_29.ogg","metal_high_high_30.ogg","metal_high_high_31.ogg","metal_high_high_32.ogg"]),
 
 ("wooden_hit_low_armor_low_damage",sf_priority_5|sf_vol_9, ["blunt_low_low_01.ogg","blunt_low_low_02.ogg","blunt_low_low_03.ogg","blunt_low_low_04.ogg","blunt_low_low_05.ogg","blunt_low_low_06.ogg","blunt_low_low_07.ogg","blunt_low_low_08.ogg","blunt_low_low_09.ogg","blunt_low_low_10.ogg"]),
 ("wooden_hit_low_armor_high_damage",sf_priority_5|sf_vol_9, ["blunt_low_high_01.ogg","blunt_low_high_02.ogg","blunt_low_high_03.ogg","blunt_low_high_04.ogg","blunt_low_high_05.ogg","blunt_low_high_06.ogg","blunt_low_high_07.ogg","blunt_low_high_08.ogg","blunt_low_high_09.ogg","blunt_low_high_10.ogg","blunt_low_high_11.ogg","blunt_low_high_12.ogg","blunt_low_high_13.ogg"]),
 ("wooden_hit_high_armor_low_damage",sf_priority_5|sf_vol_9, ["blunt_high_low_01.ogg","blunt_high_low_02.ogg","blunt_high_low_03.ogg","blunt_high_low_04.ogg","blunt_high_low_05.ogg","blunt_high_low_06.ogg","blunt_high_low_07.ogg","blunt_high_low_08.ogg","blunt_high_low_09.ogg","blunt_high_low_10.ogg"]),
 ("wooden_hit_high_armor_high_damage",sf_priority_5|sf_vol_9, ["blunt_high_high_01.ogg","blunt_high_high_02.ogg","blunt_high_high_03.ogg","blunt_high_high_04.ogg","blunt_high_high_05.ogg","blunt_high_high_06.ogg","blunt_high_high_07.ogg","blunt_high_high_08.ogg","blunt_high_high_09.ogg","blunt_high_high_10.ogg","blunt_high_high_11.ogg","blunt_high_high_12.ogg","blunt_high_high_13.ogg","blunt_high_high_14.ogg","blunt_high_high_15.ogg","blunt_high_high_16.ogg","blunt_high_high_17.ogg","blunt_high_high_18.ogg","blunt_high_high_19.ogg","blunt_high_high_20.ogg","blunt_high_high_21.ogg","blunt_high_high_22.ogg"]),

 ("mp_arrow_hit_target",sf_2d|sf_priority_10|sf_vol_9, ["mp_arrow_hit_target.wav"]),
 
 ("blunt_hit",sf_priority_5|sf_vol_10, ["horse_charge_01.ogg","horse_charge_02.ogg","horse_charge_03.ogg","horse_charge_04.ogg","horse_charge_05.ogg","horse_charge_06.ogg","horse_charge_07.ogg","horse_charge_08.ogg"]),
 ("player_hit_by_arrow",sf_priority_5|sf_vol_7, ["body_hit_1.wav","body_hit_2.wav","body_hit_3.wav","impact_body2.wav","impact_body6.wav"]),

 ("pistol_shot",sf_priority_15|sf_vol_15, []),#"fl_pistol.wav"]),
 
 # hardcoded shit.
 ("release_crossbow_medium",sf_vol_15|sf_priority_13, []),
 ("release_crossbow_far",sf_vol_15|sf_priority_12, []),
 ("bullet_hit_body",sf_priority_5|sf_vol_7, 
 ["missile_flesh_01.ogg","missile_flesh_05.ogg", "missile_flesh_07.ogg", "missile_flesh_08.ogg"]),
 ("player_hit_by_bullet",sf_priority_5|sf_vol_7, 
 ["missile_flesh_01.ogg","missile_flesh_05.ogg", "missile_flesh_07.ogg", "missile_flesh_08.ogg"]),
 
 ("man_grunt",sf_priority_4|sf_vol_4, ["man_excercise_1.wav","man_excercise_2.wav","man_excercise_4.wav"]),
 ("man_breath_hard",sf_priority_3|sf_vol_7, ["man_ugh_1.wav","man_ugh_2.wav","man_ugh_4.wav","man_ugh_7.wav","man_ugh_12.wav","man_ugh_13.wav","man_ugh_17.wav"]),
 ("man_stun",sf_priority_3|sf_vol_8, ["man_stun_new_2.ogg", "man_stun_new_1.ogg"]),
 #("man_grunt_long",sf_priority_5|sf_vol_7, ["man_grunt_1.wav","man_grunt_2.wav","man_grunt_3.wav","man_grunt_5.wav","man_grunt_13.wav","man_grunt_14.wav"]),
 
 ("man_grunt_long",sf_priority_5|sf_vol_7, [
   "man_grunt_1.wav","man_grunt_2.wav","man_grunt_3.wav","man_grunt_4.wav","man_grunt_5.wav"
  ,"man_grunt_6.wav","man_grunt_7.wav","man_grunt_8.wav","man_grunt_9.wav","man_grunt_10.wav"
  ,"man_grunt_11.wav","man_grunt_12.wav","man_grunt_13.wav","man_grunt_14.wav","man_grunt_15.wav"
  ,"man_grunt_16.wav","man_grunt_17.wav","man_grunt_18.wav","man_grunt_19.wav","man_grunt_20.wav"]),

 ("man_yell",sf_priority_7|sf_vol_8, []),
# "man_yell_4.wav","man_yell_4_2.wav","man_yell_7.wav","man_yell_9.wav","man_yell_11.wav","man_yell_13.wav","man_yell_15.wav","man_yell_16.wav","man_yell_17.wav","man_yell_20.wav",
# "man_shortyell_4.wav","man_shortyell_5.wav","man_shortyell_6.wav","man_shortyell_9.wav","man_shortyell_11.wav","man_shortyell_11b.wav",
#                        "man_yell_b_18.wav","man_yell_22.wav", "man_yell_c_20.wav"]),
## not adequate, removed: "man_yell_b_21.ogg","man_yell_b_22.ogg","man_yell_b_23.ogg"]),
#TODONOW:
 ("man_warcry",sf_priority_6, []),#"man_insult_2.ogg","man_insult_3.ogg","man_insult_7.ogg","man_insult_9.ogg","man_insult_13.ogg","man_insult_15.ogg","man_insult_16.ogg"]),

 ("horse_walk",sf_priority_6|sf_vol_5, ["horse_walk_new_01.ogg","horse_walk_new_02.ogg","horse_walk_new_03.ogg","horse_walk_new_04.ogg"]),
 ("horse_trot",sf_priority_7|sf_vol_6, ["horse_trot_new_01.ogg","horse_trot_new_02.ogg","horse_trot_new_04.ogg","horse_trot_new_03.ogg"]),
 ("horse_canter",sf_priority_8|sf_vol_7, ["horse_canter_new_01.ogg","horse_canter_new_02.ogg","horse_canter_new_03.ogg","horse_canter_new_04.ogg"]),
 ("horse_gallop",sf_priority_8|sf_vol_8, ["horse_gallop_new_01.ogg","horse_gallop_new_02.ogg","horse_gallop_new_03.ogg","horse_gallop_new_04.ogg","horse_gallop_new_05.ogg"]),
 
 
 ("horse_breath",sf_priority_1|sf_vol_4, ["horse_breath_4.wav","horse_breath_5.wav","horse_breath_6.wav","horse_breath_7.wav"]),
 ("horse_snort",sf_priority_1|sf_vol_2, ["horse_snort_1.wav","horse_snort_2.wav","horse_snort_3.wav","horse_snort_4.wav","horse_snort_5.wav"]),
 ("horse_low_whinny",sf_vol_12, ["horse_whinny-1.wav","horse_whinny-2.wav"]),
 ("block_fist",sf_priority_3|sf_vol_5, ["block_fist_3.wav","block_fist_4.wav"]),
 
 ("man_hit_blunt_weak",sf_priority_5|sf_vol_7,[#"man_hit_5.wav","man_hit_6.wav","man_hit_7.wav","man_hit_8.wav","man_hit_9.wav","man_hit_10.wav","man_hit_11.wav","man_hit_12.wav","man_hit_13.wav","man_hit_14.wav","man_hit_15.wav","man_hit_17.wav","man_hit_18.wav","man_hit_19.wav","man_hit_22.wav","man_hit_29.wav","man_hit_32.wav","man_hit_57.wav","man_hit_47.wav"]),
 "man_pain_new01.wav","man_pain_new02.wav","man_pain_new03.wav","man_pain_new04.wav","man_pain_new05.wav"
 ,"man_pain_new06.wav","man_pain_new07.wav","man_pain_new08.wav","man_pain_new09.wav","man_pain_new010.wav"
 ,"man_pain_new11.wav","man_pain_new12.wav","man_pain_new13.wav","man_pain_new14.wav","man_pain_new15.wav"
 ,"man_pain_new16.wav","man_pain_new17.wav","man_pain_new18.wav","man_pain_new19.wav","man_pain_new2.wav"
 ,"man_pain_new21.wav","man_pain_new_22.wav","man_pain_new23.wav","man_pain_new24.wav","man_pain_new25.wav"
 ]),
 
 ("man_hit_blunt_strong",sf_priority_5|sf_vol_7,[#"man_hit_5.wav","man_hit_6.wav","man_hit_7.wav","man_hit_8.wav","man_hit_9.wav","man_hit_10.wav","man_hit_11.wav","man_hit_12.wav","man_hit_13.wav","man_hit_14.wav","man_hit_15.wav","man_hit_17.wav","man_hit_18.wav","man_hit_19.wav","man_hit_22.wav","man_hit_29.wav","man_hit_32.wav","man_hit_57.wav","man_hit_47.wav"]),
 "man_pain_new01.wav","man_pain_new02.wav","man_pain_new03.wav","man_pain_new04.wav","man_pain_new05.wav"
 ,"man_pain_new06.wav","man_pain_new07.wav","man_pain_new08.wav","man_pain_new09.wav","man_pain_new010.wav"
 ,"man_pain_new11.wav","man_pain_new12.wav","man_pain_new13.wav","man_pain_new14.wav","man_pain_new15.wav"
 ,"man_pain_new16.wav","man_pain_new17.wav","man_pain_new18.wav","man_pain_new19.wav","man_pain_new2.wav"
 ,"man_pain_new21.wav","man_pain_new_22.wav","man_pain_new23.wav","man_pain_new24.wav","man_pain_new25.wav"
 ]),
 
 ("man_hit_pierce_weak",sf_priority_5|sf_vol_7,[#"man_hit_5.wav","man_hit_6.wav","man_hit_7.wav","man_hit_8.wav","man_hit_9.wav","man_hit_10.wav","man_hit_11.wav","man_hit_12.wav","man_hit_13.wav","man_hit_14.wav","man_hit_15.wav","man_hit_17.wav","man_hit_18.wav","man_hit_19.wav","man_hit_22.wav","man_hit_29.wav","man_hit_32.wav","man_hit_57.wav","man_hit_47.wav"]),
 "man_pain_new01.wav","man_pain_new02.wav","man_pain_new03.wav","man_pain_new04.wav","man_pain_new05.wav"
 ,"man_pain_new06.wav","man_pain_new07.wav","man_pain_new08.wav","man_pain_new09.wav","man_pain_new010.wav"
 ,"man_pain_new11.wav","man_pain_new12.wav","man_pain_new13.wav","man_pain_new14.wav","man_pain_new15.wav"
 ,"man_pain_new16.wav","man_pain_new17.wav","man_pain_new18.wav","man_pain_new19.wav","man_pain_new2.wav"
 ,"man_pain_new21.wav","man_pain_new_22.wav","man_pain_new23.wav","man_pain_new24.wav","man_pain_new25.wav"
 ]),
 
 ("man_hit_pierce_strong",sf_priority_5|sf_vol_7, [#"man_hit_5.wav","man_hit_6.wav","man_hit_7.wav","man_hit_8.wav","man_hit_9.wav","man_hit_10.wav","man_hit_11.wav","man_hit_12.wav","man_hit_13.wav","man_hit_14.wav","man_hit_15.wav","man_hit_17.wav","man_hit_18.wav","man_hit_19.wav","man_hit_22.wav","man_hit_29.wav","man_hit_32.wav","man_hit_57.wav","man_hit_47.wav"]),
 "man_pain_new01.wav","man_pain_new02.wav","man_pain_new03.wav","man_pain_new04.wav","man_pain_new05.wav"
 ,"man_pain_new06.wav","man_pain_new07.wav","man_pain_new08.wav","man_pain_new09.wav","man_pain_new010.wav"
 ,"man_pain_new11.wav","man_pain_new12.wav","man_pain_new13.wav","man_pain_new14.wav","man_pain_new15.wav"
 ,"man_pain_new16.wav","man_pain_new17.wav","man_pain_new18.wav","man_pain_new19.wav","man_pain_new2.wav"
 ,"man_pain_new21.wav","man_pain_new_22.wav","man_pain_new23.wav","man_pain_new24.wav","man_pain_new25.wav"
 ]),
 
 ("man_hit_cut_weak",sf_priority_5|sf_vol_7, [#"man_hit_5.wav","man_hit_6.wav","man_hit_7.wav","man_hit_8.wav","man_hit_9.wav","man_hit_10.wav","man_hit_11.wav","man_hit_12.wav","man_hit_13.wav","man_hit_14.wav","man_hit_15.wav","man_hit_17.wav","man_hit_18.wav","man_hit_19.wav","man_hit_22.wav","man_hit_29.wav","man_hit_32.wav","man_hit_57.wav","man_hit_47.wav"]),
 "man_pain_new01.wav","man_pain_new02.wav","man_pain_new03.wav","man_pain_new04.wav","man_pain_new05.wav"
 ,"man_pain_new06.wav","man_pain_new07.wav","man_pain_new08.wav","man_pain_new09.wav","man_pain_new010.wav"
 ,"man_pain_new11.wav","man_pain_new12.wav","man_pain_new13.wav","man_pain_new14.wav","man_pain_new15.wav"
 ,"man_pain_new16.wav","man_pain_new17.wav","man_pain_new18.wav","man_pain_new19.wav","man_pain_new2.wav"
 ,"man_pain_new21.wav","man_pain_new_22.wav","man_pain_new23.wav","man_pain_new24.wav","man_pain_new25.wav"
 ]),
 
 ("man_hit_cut_strong",sf_priority_5|sf_vol_7, [#"man_hit_5.wav","man_hit_6.wav","man_hit_7.wav","man_hit_8.wav","man_hit_9.wav","man_hit_10.wav","man_hit_11.wav","man_hit_12.wav","man_hit_13.wav","man_hit_14.wav","man_hit_15.wav","man_hit_17.wav","man_hit_18.wav","man_hit_19.wav","man_hit_22.wav","man_hit_29.wav","man_hit_32.wav","man_hit_57.wav","man_hit_47.wav"]),
 "man_pain_new01.wav","man_pain_new02.wav","man_pain_new03.wav","man_pain_new04.wav","man_pain_new05.wav"
 ,"man_pain_new06.wav","man_pain_new07.wav","man_pain_new08.wav","man_pain_new09.wav","man_pain_new010.wav"
 ,"man_pain_new11.wav","man_pain_new12.wav","man_pain_new13.wav","man_pain_new14.wav","man_pain_new15.wav"
 ,"man_pain_new16.wav","man_pain_new17.wav","man_pain_new18.wav","man_pain_new19.wav","man_pain_new2.wav"
 ,"man_pain_new21.wav","man_pain_new_22.wav","man_pain_new23.wav","man_pain_new24.wav","man_pain_new25.wav"
 ]),
 
 
 ("man_victory",sf_priority_8|sf_vol_13, [
   ["bc1.wav", fac_britain],["bc2.wav", fac_britain],["bc3.wav", fac_britain],["bc4.wav", fac_britain],["bc5.wav", fac_britain], 
   ["jap_bc1.wav", fac_france],["jap_bc2.wav", fac_france],["jap_bc3.wav", fac_france],["jap_bc4.wav", fac_france],["jap_bc5.wav", fac_france],
   ["prus_fuerkoenig1.wav", fac_prussia], ["prus_gottschuetze3.wav", fac_prussia], ["prus_fuervater2.wav", fac_prussia], ["prus_hurra1.wav", fac_prussia],["prus_schlagt2.wav", fac_prussia],
   ["jin_charge.mp3", fac_russia],["jin_fire.mp3", fac_russia],["jin_hold.mp3", fac_russia],["jin_hold.mp3", fac_russia],["jin_charge.mp3", fac_russia],
   ["rus_battlecry1.wav", fac_austria],  ["rus_battlecry2.wav", fac_austria], ["rus_battlecry3.wav", fac_austria], ["rus_battlecry4.wav", fac_austria],["rus_battlecry5.wav", fac_austria],
   ["tur_battlecry6.wav", fac_rhine], ["tur_battlecry2.wav.wav", fac_rhine], ["tur_battlecry3.wav", fac_rhine], ["tur_battlecry4.wav", fac_rhine],["tur_battlecry5.wav", fac_rhine],
   "man_victory_4.ogg","man_victory_5.ogg"]),
 ("fire_loop",sf_priority_9|sf_vol_4|sf_looping|sf_start_at_random_pos, ["Fire_Torch_Loop3.ogg"]),
 ("torch_loop",sf_priority_9|sf_vol_4|sf_looping|sf_start_at_random_pos, ["Fire_Torch_Loop3.ogg"]),
 
 ("dummy_hit",sf_priority_9,
 [
	"wood_hit_break_new_1.ogg",
	"wood_hit_break_new_1.wav",
	"wood_hit_break_new_2.wav",
	"wood_hit_break_new_3.wav",
	"wood_hit_break_new_4.wav",
	"wood_hit_break_new_6.wav",
	"wood_hit_break_new_7.wav",
	"wood_hit_break_new_8.wav",
	"wood_hit_break_new_9.wav",
	"wood_hit_break_new_5.ogg"
	
 
 ]),
 ("dummy_destroyed",sf_priority_9, [
	"wood_hit_break_new_1.ogg",
	"wood_hit_break_new_1.wav",
	"wood_hit_break_new_2.wav",
	"wood_hit_break_new_3.wav",
	"wood_hit_break_new_4.wav",
	"wood_hit_break_new_6.wav",
	"wood_hit_break_new_7.wav",
	"wood_hit_break_new_8.wav",
	"wood_hit_break_new_9.wav",
	"wood_hit_break_new_5.ogg"
 
 ]),
 
 ("gourd_destroyed",sf_priority_9, ["dummy_break_05.ogg"]),#TODO
 ("tutorial_fail", sf_2d|sf_vol_7,["cue_failure.ogg"]),
 ("your_flag_taken", sf_2d|sf_priority_15|sf_vol_8, ["your_flag_taken.ogg"]),
 ("enemy_flag_taken", sf_2d|sf_priority_15|sf_vol_8, ["enemy_flag_taken.ogg"]),
 ("flag_returned", sf_2d|sf_priority_15|sf_vol_8, ["your_flag_returned.ogg"]),
 ("team_scored_a_point", sf_2d|sf_priority_15|sf_vol_8, ["you_scored_a_point.ogg"]),
 ("enemy_scored_a_point", sf_2d|sf_priority_15|sf_vol_8, ["enemy_scored_a_point.ogg"]),

 ("woman_grunt",sf_priority_4|sf_vol_4, 
 ["woman_exercise_1.wav","woman_exercise_2.wav","woman_exercise_3.wav","woman_exercise_4.wav",
 "woman_exercise_5.wav","woman_exercise_6.wav","woman_exercise_7.wav","woman_exercise_8.wav"]),
 
 ("woman_victory",sf_priority_8|sf_vol_13, [
   ["brit_f_battlecry_1.wav", fac_britain],["brit_f_battlecry_2.wav", fac_britain],["brit_f_battlecry_3.wav", fac_britain],["brit_f_battlecry_4.wav", fac_britain],["brit_f_battlecry_5.wav", fac_britain], 
   ["french_f_battlecry_1.wav", fac_france],["french_f_battlecry_2.wav", fac_france],["french_f_battlecry_3.wav", fac_france],["french_f_battlecry_4.wav", fac_france],["french_f_battlecry_5.wav", fac_france],
   ["prus_f_battlecry_1.wav", fac_prussia], ["prus_f_battlecry_2.wav", fac_prussia], ["prus_f_battlecry_3.wav", fac_prussia], ["prus_f_battlecry_4.wav", fac_prussia],["prus_f_battlecry_5.wav", fac_prussia],
   ["rus_f_battlecry1.wav", fac_russia],["rus_f_battlecry2.wav", fac_russia],["rus_f_battlecry3.wav", fac_russia],["rus_f_battlecry4.wav", fac_russia],["rus_f_battlecry5.wav", fac_russia],
   ["aus_f_battlecry_1.wav", fac_austria], ["aus_f_battlecry_2.wav", fac_austria], ["aus_f_battlecry_3.wav", fac_austria], ["aus_f_battlecry_4.wav", fac_austria],
   ["prus_f_battlecry_1.wav", fac_rhine], ["prus_f_battlecry_2.wav", fac_rhine], ["prus_f_battlecry_3.wav", fac_rhine], ["prus_f_battlecry_4.wav", fac_rhine],["prus_f_battlecry_5.wav", fac_rhine]
   ]),
 

 ## MM Sounds 
 
 # Sound effects.
 ("musket", sf_priority_15|sf_vol_15,[
 "missile_fire_musket_new_1.wav",
 "missile_fire_musket_new_2.wav",
 "missile_fire_musket_new_3.wav",
 "missile_fire_musket_new_4.wav",
 "missile_fire_musket_new_5.wav",
 "missile_fire_musket_new_6.wav",
 "missile_fire_musket_new_7.wav",
 "missile_fire_musket_new_8.wav",
 "missile_fire_musket_new_10.wav",
 "missile_fire_musket_new_9.wav"
 ]),
 ("matchlock_shot_new", sf_priority_15|sf_vol_15, ["stw2_hyb_weapon_arquebus_fire_01_v1.00_gme.wav", "stw2_hyb_weapon_arquebus_fire_02_v1.00_gme.wav", "stw2_hyb_weapon_arquebus_fire_03_v1.00_gme.wav", "stw2_hyb_weapon_arquebus_fire_04_v1.00_gme.wav", "stw2_hyb_weapon_arquebus_fire_05_v1.00_gme.wav", "stw2_hyb_weapon_arquebus_fire_06_v1.00_gme.wav", "stw2_hyb_weapon_arquebus_fire_07_v1.00_gme.wav", "stw2_hyb_weapon_arquebus_fire_08_v1.00_gme.wav", "stw2_hyb_weapon_arquebus_fire_09_v1.00_gme.wav", "stw2_hyb_weapon_arquebus_fire_10_v1.00_gme.wav", "stw2_hyb_weapon_arquebus_fire_11_v1.00_gme.wav", "stw2_hyb_weapon_arquebus_fire_12_v1.00_gme.wav", "stw2_hyb_weapon_arquebus_fire_13_v1.00_gme.wav", "stw2_hyb_weapon_arquebus_fire_14_v1.00_gme.wav", "stw2_hyb_weapon_arquebus_fire_15_v1.00_gme.wav", "stw2_hyb_weapon_arquebus_fire_16_v1.00_gme.wav", "stw2_hyb_weapon_arquebus_fire_17_v1.00_gme.wav", "stw2_hyb_weapon_arquebus_fire_18_v1.00_gme.wav", "stw2_hyb_weapon_arquebus_fire_19_v1.00_gme.wav", "stw2_hyb_weapon_arquebus_fire_20_v1.00_gme.wav","matchlock1.wav"]),
 ("explosion1", sf_priority_15|sf_vol_15, ["impact.mp3","impact_b.mp3"]),
 ("rifle", sf_priority_15|sf_vol_15, ["matchlock1.wav","matchlock2.wav","matchlock3.wav"]),
 ("matchlock", sf_priority_15|sf_vol_15, ["rifle_shot_e.ogg"]),
 ("flintlock", sf_priority_15|sf_vol_15, ["flintlock1.wav","flintlock2.wav","flintlock3.wav","flintlock4.wav","flintlock5.wav","flintlock6.wav","flintlock7.wav","flintlock8.wav","flintlock9.wav"]),
 ("blunderbuss", sf_priority_15|sf_vol_15, ["blunderbuss.ogg","pistol_shot_b_2.ogg","fl_pistol_arquebuse.wav"]),
 ("pistol", sf_priority_15|sf_vol_15,["pistol_shot_a_1.ogg", "pistol_shot_a_2.ogg", "pistol_shot_a_3.ogg","pistol_shot_b_1.ogg", "pistol_shot_b_2.ogg", "pistol_shot_b_3.ogg"]),
 ("pistol2", sf_priority_15|sf_vol_15,["matchlock1.wav"]),
 ("gatling", sf_priority_15|sf_vol_15,["m249.wav"]),
 ("reload_pistol",sf_priority_1|sf_vol_2, ["missile_reload_musket_new.wav"]),
 ("rocketluncher", sf_priority_15|sf_vol_5,["artillery_rocket_01.wav","artillery_rocket_02.wav","artillery_rocket_03.wav"]),
 ("cannon", sf_priority_15|sf_vol_15, 
 [
 "cannon_new_1.ogg",
 "cannon_new_2.ogg",
 "cannon_new_3.ogg",
 "cannon_new_4.ogg",
 "cannon_new_5.ogg",
 "cannon_new_6.ogg"]),
 ("rocket_launch", sf_priority_15|sf_vol_15, ["artillery_fire_rocket_new_1.wav","artillery_fire_rocket_new_2.wav"]),
 ("cannon_hit", sf_priority_7|sf_vol_13, 
 ["artillery_hit_person_01.wav",
  "artillery_hit_person_02.wav",
  "artillery_hit_person_03.wav",
  "artillery_hit_person_04.wav",
  "artillery_hit_person_05.wav",
  "artillery_hit_person_06.wav",
  "artillery_hit_person_07.wav",
  "artillery_hit_person_08.wav"
 ]), 
 ("cannon_hit_ground",sf_priority_7|sf_vol_11, ["cannonhitground.ogg"]),
 ("cannon_hit_wall",sf_priority_10|sf_vol_15, ["artillery_hit_wall_01.wav","artillery_hit_wall_02.wav"]),
 ("cannon_hit_wood_wall",sf_priority_10|sf_vol_15, ["artillery_hit_wood_01.wav","artillery_hit_wood_02.wav","artillery_hit_wood_03.wav","artillery_hit_wood_04.wav",]),
 ("cannon_fuse",sf_vol_6, ["dedal_grenade_fuse.ogg", "boe_fuse_01.ogg"]),
 ("cannon_ball",sf_vol_5, ["artillery_cannonball_input.ogg"]),
 ("explosion",sf_priority_15|sf_vol_15, ["explosion_boom_new_1.wav","explosion_boom_new_4.wav","explosion_boom_new_3.ogg","explosion_boom_new_5.ogg", "boe_explosion_1.ogg", "boe_explosion_2.ogg"]),
 ("holy_call",sf_priority_10|sf_vol_15, ["holy_grenade.ogg"]),
 ("admin_banhammer",sf_priority_15|sf_vol_15|sf_2d, ["admin_banhammer.ogg"]),
 ("admin_shotgun",sf_priority_15|sf_vol_15|sf_2d, ["admin_shotgun.ogg"]),
 ("admin_rocketlauncher",sf_priority_15|sf_vol_15|sf_2d, ["admin_rocketlauncher.ogg"]),
 ("glass_break",sf_priority_7|sf_vol_13, ["break_glass_01.wav","break_glass_02.wav","break_glass_03.wav","break_glass_04.wav","break_glass_05.wav","break_glass_06.wav"]),
 ("flag_loop",sf_priority_7|sf_vol_8|sf_looping, ["flagloop.wav"]),
 
 ("thunder",sf_priority_15|sf_vol_15|sf_2d, 
 ["ambient_sound_new_thunder_1.ogg",
  "ambient_sound_new_thunder_2.ogg",
  "ambient_sound_new_thunder_3.ogg",
  "ambient_sound_new_thunder_4.ogg",
  "ambient_sound_new_thunder_5.ogg",
  "ambient_sound_new_thunder_6.ogg"
 ]),

 ("crate_fuse",sf_priority_7|sf_vol_10, ["explosion_ignite_fuse_new.ogg"]),
 ("bandaging",sf_priority_7|sf_vol_10, ["bandaging1.ogg","bandaging1_1.ogg"]),
 ("church_bell",sf_priority_15|sf_vol_15, ["churchbells_ring_new.wav"]),
 ("boat_sinking",sf_priority_7|sf_vol_13|sf_stream_from_hd, ["boat_sinking.ogg"]),

 # ball/rocket flight loop sounds.
 ("cannonball_loop",sf_priority_15|sf_vol_5|sf_looping, ["ball_loop.wav"]),
 ("rocket_loop",sf_priority_15|sf_vol_6|sf_looping, ["explosion_ignite_fuse_new.ogg"]),

 ("hammer",sf_vol_7, ["hammer1.wav","hammer3.wav","hammer2.wav"]),
 ("shovel",sf_vol_15, ["boe_digging_01.ogg","boe_digging_02.ogg","boe_digging_03.ogg","boe_digging_04.ogg","boe_digging_05.ogg"]),
 ("ramrod",sf_vol_12, ["artillery_reload_cannonball_new.wav"]),

 ("door_open",sf_vol_5, ["door_open_new.ogg"]),
 ("door_close",sf_vol_5, ["door_close_new.ogg"]),
 ("door_lock",sf_vol_5, ["door_lock_new.ogg"]),

 ("underwater_noise",sf_2d|sf_priority_7|sf_vol_7|sf_looping, ["underwater.wav"]),
 ("drown",sf_priority_7|sf_vol_7, ["gurgle1.wav","gurgle2.wav","gurgle3.wav","gurgle4.wav","gurgle5.wav","gurgle6.wav","gurgle7.wav","gurgle8.wav","gurgle9.wav","gurgle10.wav"]),
 ("come_up",sf_priority_7|sf_vol_7, ["dedal_breath.ogg"]),
 
 #Ambience #
 ("ambient_birds",sf_vol_6|sf_priority_15|sf_looping|sf_start_at_random_pos, ["ambient_sound_new_bird.ogg", "ambient_sound_new_bird_2.ogg"]),
 ("ambient_birds_many",sf_vol_6|sf_priority_15|sf_looping|sf_start_at_random_pos, ["ambient_sound_new_bird.ogg", "ambient_sound_new_bird_2.ogg"]),
 ("ambient_ocean",sf_vol_10|sf_priority_15|sf_looping|sf_start_at_random_pos, ["oceanwaves.wav"]),
 ("ambient_crickets_many",sf_vol_6|sf_priority_15|sf_looping|sf_start_at_random_pos, ["crickets_many.wav"]),
 ("ambient_crickets_few",sf_vol_6|sf_priority_15|sf_looping|sf_start_at_random_pos, ["crickets.wav"]),  
 ("ambient_river",sf_vol_11|sf_priority_15|sf_looping|sf_start_at_random_pos, ["river.wav"]),
 ("ambient_seagulls",sf_vol_6|sf_priority_15|sf_looping|sf_start_at_random_pos, ["seagulls.wav"]), 
 ("ambient_fly",sf_vol_6|sf_priority_8|sf_looping|sf_start_at_random_pos, ["fly.wav"]), 
 ("ambient_night",sf_vol_6|sf_priority_15|sf_looping|sf_start_at_random_pos, ["ambient_sound_new_forest.wav"]), 
 ("ambient_roof",sf_vol_6|sf_priority_15|sf_looping|sf_start_at_random_pos, ["Rain_heavy_roof.wav"]),
 ("ambient_stone",sf_vol_6|sf_priority_15|sf_looping|sf_start_at_random_pos, ["Rain_heavy_stone.wav"]),
 ("ambient_windmill",sf_vol_6|sf_priority_15|sf_looping|sf_start_at_random_pos, ["windmill_fan.wav"]),

 #global ambients, new sound system.
 ("global_ambient_night",sf_2d|sf_vol_10|sf_priority_15|sf_looping|sf_stream_from_hd, ["ambient_sound_new_night_plain.ogg", "ambient_sound_new_night_plain_2.ogg"]), 
 ("global_ambient_beach",sf_2d|sf_vol_10|sf_priority_15|sf_looping|sf_stream_from_hd, ["beach.ogg"]), 
 ("global_ambient_farmland",sf_2d|sf_vol_10|sf_priority_15|sf_looping|sf_stream_from_hd, ["day_1.wav"]), 
 ("global_ambient_farmland_evening",sf_2d|sf_vol_10|sf_priority_15|sf_looping|sf_stream_from_hd, ["ambient_sound_new_plain.ogg","ambient_sound_new_plain_2.ogg" ]), 
 ("global_ambient_farmland_empty",sf_2d|sf_vol_10|sf_priority_15|sf_looping|sf_stream_from_hd, ["empty_farmland.ogg"]), 
 ("global_ambient_city_empty",sf_2d|sf_vol_10|sf_priority_15|sf_looping|sf_stream_from_hd, ["empty_city.ogg"]), 

 ("ambient_buzzard",sf_vol_15|sf_priority_15, ["ambient_sound_new_goose.ogg"]),
 ("ambient_crow",sf_vol_15|sf_priority_15, ["ambient_sound_new_crow.ogg"]),
 
 # Win/loose sounds.
 ("win_tune_brit", sf_2d|sf_priority_15|sf_vol_8|sf_stream_from_hd, ["win_ming.mp3","ming_win.ogg"]),
 ("win_tune_fren", sf_2d|sf_priority_15|sf_vol_8|sf_stream_from_hd, ["victory_japan.ogg"]),
 ("win_tune_prus", sf_2d|sf_priority_15|sf_vol_8|sf_stream_from_hd, ["won1_x2.mp3"]),
 ("win_tune_russ", sf_2d|sf_priority_15|sf_vol_8|sf_stream_from_hd, ["win_jin.mp3"]),
 ("win_tune_aust", sf_2d|sf_priority_15|sf_vol_8|sf_stream_from_hd, ["win_rus.mp3"]),
 ("win_tune_rhen", sf_2d|sf_priority_15|sf_vol_8|sf_stream_from_hd, ["ceddin_deden.ogg"]),
 
 ("loose_tune_brit", sf_2d|sf_priority_15|sf_vol_8|sf_stream_from_hd, ["ming_lose.mp3"]),
 ("loose_tune_fren", sf_2d|sf_priority_15|sf_vol_8|sf_stream_from_hd, ["lose_sound_new_1.ogg"]),
 ("loose_tune_prus", sf_2d|sf_priority_15|sf_vol_8|sf_stream_from_hd, ["lose_sound_new_2.ogg"]),
 ("loose_tune_russ", sf_2d|sf_priority_15|sf_vol_8|sf_stream_from_hd, ["lose_sound_new_2.ogg"]),
 ("loose_tune_aust", sf_2d|sf_priority_15|sf_vol_8|sf_stream_from_hd, ["lose_sound_new_3.ogg"]),
 ("loose_tune_rhen", sf_2d|sf_priority_15|sf_vol_8|sf_stream_from_hd, ["lose_sound_new_3.ogg"]),
 
  # battle cries.
 ("voice_cry_brit", sf_priority_8|sf_vol_13, [
    "bc1.wav",# Great Ming!
    "bc2.wav",
    "bc3.wav",
    "bc4.wav",
    "bc5.wav",
    "ming_bc1.mp3",
    "ming_bc2.mp3",
    "bc6.wav"
 ]), 
 
 ("voice_cry_fren", sf_priority_8|sf_vol_13, ["jap_bc1.wav","jap_bc2.wav","jap_bc3.wav","jap_bc4.wav","jap_bc5.wav","man_shout_jap_01.wav", "man_shout_jap_02.wav", "man_shout_jap_03.wav", "man_shout_jap_04.wav", "man_shout_jap_05.wav", "man_shout_jap_06.wav", "man_shout_jap_07.wav", "man_shout_jap_08.wav", "man_shout_jap_09.wav", "man_shout_jap_10.wav", "man_shout_jap_11.wav", "man_shout_jap_12.wav", "man_shout_jap_13.wav", "man_shout_jap_14.wav", "man_shout_jap_15.wav", "man_shout_jap_16.wav", "man_shout_jap_17.wav", "man_shout_jap_18.wav"]),
 ("voice_cry_prus", sf_priority_8|sf_vol_13, [
    "prus_fuerkoenig1.wav" # Fur Konig und Vaterland !
   ,"prus_fuerkoenig2.wav"
   ,"prus_gottschuetze1.wav" # Gott schutze den Konig !
   ,"prus_gottschuetze2.wav"
   ,"prus_gottschuetze3.wav"
   ,"prus_fuervater1.wav" # Fur das Vaterland !
   ,"prus_fuervater2.wav"
   ,"prus_fuervater3.wav"
   ,"prus_fuervater4.wav" 
   ,"prus_schlagt1.wav" # Schlagt sie !
   ,"prus_schlagt2.wav"
   ,"prus_hurra1.wav"	# Hurra !
   ,"prus_hurra2.wav"
   ,"prus_hurra3.wav"
   ,"prus_hurra4.wav"
   ,"prus_aufgehts1.wav" # Auf gehts Kameraden !
   ,"prus_aufgehts2.wav"
 ]),
 ("voice_cry_russ", sf_priority_8|sf_vol_13, [
    "jin_charge.mp3"
   ,"jin_fire.mp3"
   ,"jin_hold.mp3"
 ]),
 ("voice_cry_aust", sf_priority_8|sf_vol_13, [
    "rus_battlecry1.wav"
   ,"rus_battlecry2.wav"
   ,"rus_battlecry3.wav"
   ,"rus_battlecry4.wav"
   ,"rus_battlecry5.wav"
   ,"rus_battlecry6.wav"
   ,"rus_battlecry7.wav"
   ,"rus_battlecry8.wav"
   ,"rus_battlecry9.wav"
   ,"rus_battlecry10.wav"
   ,"rus_battlecry11.wav"
   ,"rus_battlecry12.wav"
   ,"rus_battlecry13.wav"
 ]),
 ("voice_cry_brit_scot", sf_priority_8|sf_vol_13, [
    "brit_bastard1.wav" # Come on yer bastards
   ,"brit_bastard2.wav"
   ,"brit_scotland1.wav" # Scotland Ferever
   ,"brit_scotland2.wav" 
   ,"brit_sonsof1.wav" # Sons of the hounds, come here and get flesh
   ,"brit_sonsof2.wav"
   ,"brit_bydand1.wav" # Bydand
   ,"brit_bydand2.wav"
 ]),
 ("voice_cry_russ_ukr", sf_priority_8|sf_vol_13, [
    "ukr_battlecry1.wav" 
   ,"ukr_battlecry2.wav"
   ,"ukr_battlecry3.wav"
   ,"rus_battlecry3.wav"
   ,"rus_battlecry10.wav"
   ,"rus_battlecry11.wav"
   ,"rus_battlecry12.wav"
 ]),
 ("voice_cry_rhen", sf_priority_8|sf_vol_13, [
    "tur_battlecry2.wav"
   ,"tur_battlecry3.wav"
   ,"tur_battlecry4.wav"
   ,"tur_battlecry5.wav"
   ,"tur_battlecry6.wav"
   ,"tur_battlecry7.wav"
   ,"tur_battlecry8.wav"
   ,"tur_battlecry9.wav"
   ,"tur_battlecry10.wav"
   ,"tur_battlecry11.wav"
   ,"tur_battlecry12.wav"
   ,"tur_battlecry13.wav"
 ]),
 
 ("voice_cry_pirate", sf_priority_8|sf_vol_13, [
    "pirate_1.wav"
   ,"pirate_2.wav"
   ,"pirate_3.wav"
   ,"pirate_4.wav"
   ,"pirate_5.wav"
   ,"pirate_6.wav"
   ,"pirate_7.wav"
   ,"pirate_8.wav"
   ,"pirate_9.wav"
   ,"pirate_10.wav"
   ,"pirate_11.wav"
   ,"pirate_12.wav"
   ,"pirate_13.wav"
   ,"pirate_14.wav"
 ]), 
 
 ("voice_cry_qi_army", sf_priority_8|sf_vol_13, [
   "qi_army_bc.wav",# Great Ming!Qi army
    "bc1.wav",
    "bc2.wav",
    "bc3.wav",
    "bc4.wav",
    "bc5.wav",
    "bc6.wav"
 ]), 
 
 ("voice_cry_baigan", sf_priority_8|sf_vol_13, [         
    "b1.wav",# Great Ming!Baigan
    "b2.wav",
    "b3.wav",
    "b4.wav",
    "b5.wav",
    "b6.wav",
    "b7.wav",
    "b8.wav",
    "b9.wav",
    "b10.wav",
    "b11.wav",
    "b12.wav"
 ]), 
 
 
 # Surrendering
 ("voice_surrender_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, [
     "ming_surr1.mp3" 
    ,"ming_surr2.mp3"
    ,"ming_surr3.mp3"
    ,"ming_surr4.mp3" 
   # ,"brit_dont2.wav"
   # ,"brit_dont3.wav"
   # ,"brit_spare1.wav" # Spare me!
   # ,"brit_spare2.wav"
 ]),
 ("voice_surrender_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["man_shout_jap_needmedic_01.wav"]),
 ("voice_surrender_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, [
    "prus_ichergebe1.wav" # Ich ergebe mich !
   ,"prus_ichergebe2.wav"
   ,"prus_ichergebe3.wav"
   ,"prus_ichgebe1.wav" # Ich gebe auf !
   ,"prus_nichtschiessen1.wav" # Nicht schiessen !
   ,"prus_nichtschiessen2.wav"
 ]),
 ("voice_surrender_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, [
     "jin_surrender.mp3"
   # ,"rus_surrender2.wav"
   # ,"rus_surrender3.wav"
   # ,"rus_surrender4.wav"
   # ,"rus_surrender5.wav"
   # ,"rus_surrender6.wav"
   # ,"rus_surrender7.wav"
   # ,"rus_surrender8.wav"
 ]),
  ("voice_surrender_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, [
    # "ukr_surrender1.wav"
   # ,"ukr_surrender2.wav"
   # ,"ukr_surrender3.wav"
   # ,"ukr_surrender4.wav"
 ]),
 
 # # Officer commands # #
 
 #Inf
 ("voice_comm_inf", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_inf.mp3"]),
 ("voice_comm_inf2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_infanteria1.mp3","orden_infanteria2.mp3"]),
 ("voice_comm_inf3", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_infanteria1.mp3","orden_infanteria2.mp3"]),
 ("voice_comm_inf4", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_infanteria1.mp3","orden_infanteria2.mp3"]),
 ("voice_comm_inf5", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_infanteria1.mp3","orden_infanteria2.mp3"]),
 ("voice_comm_inf", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_infanteria1.mp3","orden_infanteria2.mp3"]),
 #Skr
 ("voice_comm_skr", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_aqueros1.mp3","orden_aqueros2.mp3"]),
 ("voice_comm_skr2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_aqueros1.mp3","orden_aqueros2.mp3"]),
 ("voice_comm_skr3", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_aqueros1.mp3","orden_aqueros2.mp3"]),
 ("voice_comm_skr4", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_aqueros1.mp3","orden_aqueros2.mp3"]),
 ("voice_comm_skr5", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_aqueros1.mp3","orden_aqueros2.mp3"]),
 ("voice_comm_skr6", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_aqueros1.mp3","orden_aqueros2.mp3"]),
 #Cav
 ("voice_comm_cav", sf_priority_8|sf_vol_13|sf_stream_from_hd, [" orden_caballeria1.mp3"," orden_caballeria2.mp3"]),
 ("voice_comm_cav2", sf_priority_8|sf_vol_13|sf_stream_from_hd, [" orden_caballeria1.mp3"," orden_caballeria2.mp3"]),
 ("voice_comm_cav3", sf_priority_8|sf_vol_13|sf_stream_from_hd, [" orden_caballeria1.mp3"," orden_caballeria2.mp3"]),
 ("voice_comm_cav4", sf_priority_8|sf_vol_13|sf_stream_from_hd, [" orden_caballeria1.mp3"," orden_caballeria2.mp3"]),
 ("voice_comm_cav5", sf_priority_8|sf_vol_13|sf_stream_from_hd, [" orden_caballeria1.mp3"," orden_caballeria2.mp3"]),
 ("voice_comm_cav6", sf_priority_8|sf_vol_13|sf_stream_from_hd, [" orden_caballeria1.mp3"," orden_caballeria2.mp3"]),
 
 #unit
 ("voice_comm_unit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["soldados.ogg"]),
 ("voice_comm_unit2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["soldados.ogg"]),
 ("voice_comm_unit3", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["soldados.ogg"]),
 ("voice_comm_unit4", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["soldados.ogg"]),
 ("voice_comm_unit5", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["soldados.ogg"]),
 ("voice_comm_unit6", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["soldados.ogg"]),
 #everyone
 ("voice_comm_every", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["soldados.ogg"]),
 ("voice_comm_every2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["soldados.ogg"]),
 ("voice_comm_every3", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["soldados.ogg"]),
 ("voice_comm_every4", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["soldados.ogg"]),
 ("voice_comm_every5", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["soldados.ogg"]),
 ("voice_comm_every6", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["soldados.ogg"]),
 ("voice_comm_every7", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["soldados.ogg"]),
 
 
 # Make Ready
 ("voice_comm_ready_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["yuanchengwuqi.wav"]),
 ("voice_comm_ready_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jap_range.wav"]),
 ("voice_comm_ready_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["prus_bereit1.wav","prus_bereit2.wav","prus_bereit3.wav","prus_bereit4.wav","prus_bereit5.wav"]),
 ("voice_comm_ready_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_at_my_command.mp3"]),
 ("voice_comm_ready_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ukr_ready1.wav","ukr_ready2.wav"]),
 ("voice_comm_ready_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_linia.mp3"]),
 ("voice_comm_ready_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["tur_ready1.wav","tur_ready2.wav","tur_ready3.wav"]),
 ("voice_comm_ready_russ2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["rus_ready1.wav","rus_ready2.wav","rus_ready3.wav"]),
 # Present
 ("voice_comm_present_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["tinglingkaihuo.wav"]),
 ("voice_comm_present_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jap_ready3.mp3"]),
 ("voice_comm_present_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["prus_anlegen1.wav","prus_anlegen2.wav","prus_anlegen3.wav","prus_anlegen4.wav"]),
 ("voice_comm_present_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_range.mp3"]),
 ("voice_comm_present_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ukr_present1.wav","ukr_present2.wav"]),
 ("voice_comm_present_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_linia.mp3"]),
 ("voice_comm_present_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["tur_present1.wav","tur_present2.wav"]),
 ("voice_comm_present_russ2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["rus_present1.wav","rus_present2.wav"]),
 # Fire
 ("voice_comm_fire_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["quantikaihuo.wav","all_fire.wav"]),
 ("voice_comm_fire_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["man_shout_jap_fire_01.wav","man_shout_jap_fire_02.wav","man_shout_jap_fire_03.wav","man_shout_jap_fire_04.wav"]),
 ("voice_comm_fire_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_disparo.mp3","orden_disparo1.mp3","orden_disparo2.mp3","orden_disparo3.mp3"]),
 ("voice_comm_fire_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_fire.mp3"]),
 ("voice_comm_fire_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ukr_fire1.wav","ukr_fire2.wav"]),
 ("voice_comm_fire_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_disparo.mp3","orden_disparo1.mp3","orden_disparo2.mp3","orden_disparo3.mp3"]),
 ("voice_comm_fire_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["tur_fire1.wav","tur_fire2.wav","tur_fire3.wav"]),
 ("voice_comm_fire_russ2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["rus_fire1.wav","rus_fire2.wav","rus_fire3.wav"]),
 # Fire left
 ("voice_comm_fire_left_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["zuoyikaihuo.wav"]),
 ("voice_comm_fire_left_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["man_shout_jap_fire_01.wav","man_shout_jap_fire_02.wav","man_shout_jap_fire_03.wav","man_shout_jap_fire_04.wav"]),
 ("voice_comm_fire_left_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_disparo.mp3","orden_disparo1.mp3","orden_disparo2.mp3","orden_disparo3.mp3"]),
 ("voice_comm_fire_left_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_fire_left.mp3"]),
 ("voice_comm_fire_left_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ukr_fire1.wav","ukr_fire2.wav"]),
 ("voice_comm_fire_left_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_disparo.mp3","orden_disparo1.mp3","orden_disparo2.mp3","orden_disparo3.mp3"]),
 ("voice_comm_fire_left_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["tur_fire1.wav","tur_fire2.wav","tur_fire3.wav"]),
 ("voice_comm_fire_left_russ2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["rus_fire1.wav","rus_fire2.wav","rus_fire3.wav"]),
 # Fire middle
 ("voice_comm_fire_middle_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["zhongjunkaihuo.wav"]),
 ("voice_comm_fire_middle_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["man_shout_jap_fire_01.wav","man_shout_jap_fire_02.wav","man_shout_jap_fire_03.wav","man_shout_jap_fire_04.wav"]),
 ("voice_comm_fire_middle_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["prus_feuer1.wav","prus_feuer2.wav","prus_feuer3.wav"]),
 ("voice_comm_fire_middle_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_fire_mid.mp3"]),
 ("voice_comm_fire_middle_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ukr_fire1.wav","ukr_fire2.wav"]),
 ("voice_comm_fire_middle_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_disparo.mp3","orden_disparo1.mp3","orden_disparo2.mp3","orden_disparo3.mp3"]),
 ("voice_comm_fire_middle_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["tur_fire1.wav","tur_fire2.wav","tur_fire3.wav"]),
 ("voice_comm_fire_middle_russ2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["rus_fire1.wav","rus_fire2.wav","rus_fire3.wav"]),
 # Fire right
 ("voice_comm_fire_right_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["youyikaihuo.wav"]),
 ("voice_comm_fire_right_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["man_shout_jap_fire_01.wav","man_shout_jap_fire_02.wav","man_shout_jap_fire_03.wav","man_shout_jap_fire_04.wav"]),
 ("voice_comm_fire_right_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["prus_feuer1.wav","prus_feuer2.wav","prus_feuer3.wav"]),
 ("voice_comm_fire_right_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_fire_right.mp3"]),
 ("voice_comm_fire_right_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ukr_fire1.wav","ukr_fire2.wav"]),
 ("voice_comm_fire_right_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_disparo.mp3","orden_disparo1.mp3","orden_disparo2.mp3","orden_disparo3.mp3"]),
 ("voice_comm_fire_right_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["tur_fire1.wav","tur_fire2.wav","tur_fire3.wav"]),
 ("voice_comm_fire_right_russ2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["rus_fire1.wav","rus_fire2.wav","rus_fire3.wav"]),
 # Charge
 ("voice_comm_charge_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["chongfeng.wav","bc4.wav"]),
 ("voice_comm_charge_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["man_shout_jap_charge_01.wav", "man_shout_jap_charge_02.wav",  "man_shout_jap_charge_04.wav", "man_shout_jap_charge_05.wav","jap_charge.wav"]),
 ("voice_comm_charge_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, [" orden_carga1.mp3"," orden_carga2.mp3"," orden_carga3.mp3"," orden_carga4.mp3"]),
 ("voice_comm_charge_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_charge.mp3"]),
 ("voice_comm_charge_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["rus_charge1.wav","rus_charge2.wav","rus_charge3.wav","rus_charge4.wav"]),
 ("voice_comm_charge_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, [" orden_carga1.mp3"," orden_carga2.mp3"," orden_carga3.mp3"," orden_carga4.mp3"]),
 ("voice_comm_charge_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, [" tur_charge1.wav"," tur_charge2.wav"," tur_charge3.wav"," tur_charge4.wav","tur_charge5.wav"]),
 ("voice_comm_charge_russ2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["rus_charge1.wav","rus_charge2.wav","rus_charge3.wav","rus_charge4.wav"]),
 # Company, advance!
 ("voice_comm_advance_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["xiangqian.wav"]),
 ("voice_comm_advance_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["man_shout_jap_advance_01.wav", "man_shout_jap_advance_02.wav"]),
 ("voice_comm_advance_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["cris_3.wav", "cris_2.wav", "cris_4.wav"]),
 ("voice_comm_advance_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_forward.mp3"]),
 ("voice_comm_advance_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ukr_onme1.wav","ukr_onme2.wav"]),
 ("voice_comm_advance_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["cris_3.wav", "cris_2.wav", "cris_4.wav"]),
 ("voice_comm_advance_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["tur_advance1.wav", "tur_advance1.wav", "tur_advance1.wav","tur_advance4.wav","tur_advance5.wav"]),
 ("voice_comm_advance_russ2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["rus_advance1.wav","rus_advance2.wav","rus_advance3.wav","rus_advance4.wav","rus_advance5.wav"]),
 # Hold this position!
 ("voice_comm_hold_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jianshouzhendi.wav"]),
 ("voice_comm_hold_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jap_hold.wav"]),
 ("voice_comm_hold_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_posicion.mp3"]),
 ("voice_comm_hold_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_hold.mp3"]),
 ("voice_comm_hold_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ukr_holdpos1.wav","ukr_holdpos2.wav","ukr_holdpos3.wav"]),
 ("voice_comm_hold_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_posicion.mp3"]),
 ("voice_comm_hold_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["tur_holdpos1.wav","tur_holdpos2.wav","tur_holdpos3.wav"]),
  ("voice_comm_hold_russ2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["rus_holdpos1.wav","rus_holdpos2.wav","rus_holdpos3.wav"]),
 # Fire at will!
 ("voice_comm_fire_at_will_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["quantikaihuo.wav"]),
 ("voice_comm_fire_at_will_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["man_shout_jap_fire_01.wav", "man_shout_jap_fire_02.wav", "man_shout_jap_fire_03.wav", "man_shout_jap_fire_04.wav"]),
 ("voice_comm_fire_at_will_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_disparo.mp3","orden_disparo1.mp3","orden_disparo2.mp3","orden_disparo3.mp3"]),
 ("voice_comm_fire_at_will_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_fire_at_will.mp3"]),
 ("voice_comm_fire_at_will_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ukr_fireatwill1.wav"]),
 ("voice_comm_fire_at_will_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_disparo.mp3","orden_disparo1.mp3","orden_disparo2.mp3","orden_disparo3.mp3"]),
 ("voice_comm_fire_at_will_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["tur_fire1.wav","tur_fire2.wav","tur_fire3.wav"]),
 ("voice_comm_fire_at_will_russ2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["rus_fireatwill1.wav","rus_fireatwill2.wav"]),
 # Company, on me! 
 ("voice_comm_on_me_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["gensui.wav"]),
 ("voice_comm_on_me_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["man_shout_jap_onme_01.wav", "man_shout_jap_onme_02.wav","jap_onme.wav"]),
 ("voice_comm_on_me_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_seguidme.mp3", "orden_seguidme1.mp3", "orden_seguidme2.mp3", "orden_seguidme3.mp3", "orden_seguidme4.mp3", "orden_seguidme5.mp3", "orden_seguidme6.mp3"]),
 ("voice_comm_on_me_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_follow.mp3"]),
 ("voice_comm_on_me_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ukr_onme1.wav","ukr_onme2.wav","ukr_onme3.wav","ukr_onme4.wav"]),
 ("voice_comm_on_me_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_seguidme.mp3", "orden_seguidme1.mp3", "orden_seguidme2.mp3", "orden_seguidme3.mp3", "orden_seguidme4.mp3", "orden_seguidme5.mp3", "orden_seguidme6.mp3"]),
 ("voice_comm_on_me_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_on_me_russ2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["rus_onme1.wav","rus_onme2.wav","rus_onme3.wav"]),
 
 
 # Fall back!
 ("voice_comm_fall_back_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["chetui1.wav","chetui2.wav"]),
 ("voice_comm_fall_back_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["man_shout_jap_retreat_01.wav", "man_shout_jap_retreat_02.wav","jap_fallback.wav"]),
 ("voice_comm_fall_back_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["retreat.mp3"]),
 ("voice_comm_fall_back_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_retreat.mp3"]),
 ("voice_comm_fall_back_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ukr_all_retreat1.wav","ukr_retreat1.wav","ukr_fallback1.wav"]),
 ("voice_comm_fall_back_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["retreat.mp3"]),
 ("voice_comm_fall_back_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["tur_retreat1.wav","tur_all_retreat1.wav"]),
 ("voice_comm_fall_back_russ2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["rus_all_retreat1.wav","rus_retreat1.wav","rus_fallback1.wav"]),
 #Mount
 ("voice_comm_fall_mount_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["shangma.wav"]),
 ("voice_comm_fall_mount_jap", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jap_mount.mp3"]),
 ("voice_comm_fall_mount_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_mount_jin", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_mount.mp3"]),
 ("voice_comm_fall_mount_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_mount_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_mount_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_mount_russ2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 #Dismount
 ("voice_comm_fall_dismount_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["xiama.wav"]),
 ("voice_comm_fall_dismount_jap", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jap_dismount.mp3"]),
 ("voice_comm_fall_dismount_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_dismount_jin", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_dismount.mp3"]),
 ("voice_comm_fall_dismount_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_dismount_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_dismount_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_dismount_tur2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 #Stand closer
 ("voice_comm_fall_closer_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["julong.wav"]),
 ("voice_comm_fall_closer_jap", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jap_close.mp3"]),
 ("voice_comm_fall_closer_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_closer_jin", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_close.mp3"]),
 ("voice_comm_fall_closer_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_closer_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_closer_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_closer_tur2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 #Spread
 ("voice_comm_fall_spread_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["sankai.wav"]),
 ("voice_comm_fall_spread_jap", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jap_spread.mp3"]),
 ("voice_comm_fall_spread_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_spread_jin", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_spread.mp3"]),
 ("voice_comm_fall_spread_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_spread_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_spread_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_spread_tur2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 #Use any weapon
 ("voice_comm_fall_any_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ziyoukaihuo.wav"]),
 ("voice_comm_fall_any_jap", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jap_melee.mp3"]),
 ("voice_comm_fall_any_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_any_jin", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_any.mp3"]),
 ("voice_comm_fall_any_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_any_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_any_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_any_tur2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 #1 row
 ("voice_comm_fall_1_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["1row.wav"]),
 ("voice_comm_fall_1_jap", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jap_1row.mp3"]),
 ("voice_comm_fall_1_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_1_jin", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_1row.mp3"]),
 ("voice_comm_fall_1_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_1_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 ("voice_comm_fall_1_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 ("voice_comm_fall_1_tur2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 #2 row
 ("voice_comm_fall_2_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["2row.wav"]),
 ("voice_comm_fall_2_jap", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jap_2row.mp3"]),
 ("voice_comm_fall_2_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_2_jin", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_2row.mp3"]),
 ("voice_comm_fall_2_any_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_2_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 ("voice_comm_fall_2_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 ("voice_comm_fall_2_tur2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 #3 row
 ("voice_comm_fall_3_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["3row.wav"]),
 ("voice_comm_fall_3_jap", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jap_3row.mp3"]),
 ("voice_comm_fall_3_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_3_jin", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_3row.mp3"]),
 ("voice_comm_fall_3_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_3_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 ("voice_comm_fall_3_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 ("voice_comm_fall_3_tur2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 #4 row
 ("voice_comm_fall_4_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["4row.wav"]),
 ("voice_comm_fall_4_jap", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jap_4row.mp3"]),
 ("voice_comm_fall_4_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_4_jin", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_4row.mp3"]),
 ("voice_comm_fall_4_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_4_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 ("voice_comm_fall_4_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 ("voice_comm_fall_4_tur2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 #5 row
 ("voice_comm_fall_5_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["5row.wav"]),
 ("voice_comm_fall_5_jap", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jap_5row.mp3"]),
 ("voice_comm_fall_5_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_5_jin", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_5row.mp3"]),
 ("voice_comm_fall_5_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_5_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 ("voice_comm_fall_5_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 ("voice_comm_fall_5_tur2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 #Hold fire
 ("voice_comm_fall_hold_fire_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["tingzhikaihuo.wav"]),
 ("voice_comm_fall_hold_fire_jap", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jap_stop.mp3"]),
 ("voice_comm_fall_hold_fire_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_hold_fire_jin", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_hold_fire.mp3"]),
 ("voice_comm_fall_hold_fire_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_hold_fire_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 ("voice_comm_fall_hold_fire_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 ("voice_comm_fall_hold_fire_tur2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 # Female voices.

 #Melee
 ("voice_comm_fall_melee_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jinzhan.wav"]),
 ("voice_comm_fall_melee_jap", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jap_melee.mp3"]),
 ("voice_comm_fall_melee_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_melee_jin", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_melee.mp3"]),
 ("voice_comm_fall_melee_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_melee_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),  
 ("voice_comm_fall_melee_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),  
 ("voice_comm_fall_melee_tur2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 #Range weapon
 ("voice_comm_fall_range_weapon_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["yuanchengwuqi.wav"]),
 ("voice_comm_fall_range_weapon_jap", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jap_range.mp3"]),
 ("voice_comm_fall_range_weapon_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_range_weapon_jin", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_range.mp3"]),
 ("voice_comm_fall_range_weapon_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_range_weapon_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 ("voice_comm_fall_range_weapon_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 ("voice_comm_fall_range_weapon_tur2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 #Retreat
 ("voice_comm_fall_retreat_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["chetui1.wav","chetui2.wav"]),
 ("voice_comm_fall_retreat_jap", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jap_fallback.wav"]),
 ("voice_comm_fall_retreat_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_retreat_jin", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_retreat","jin_retreat2"]),
 ("voice_comm_fall_retreat_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_retreat_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 ("voice_comm_fall_retreat_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["tur_retreat1.wav","tur_all_retreat1.wav"]), 
 ("voice_comm_fall_retreat_tur2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 #Stand_ground
 ("voice_comm_stand_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["zhanzaiyuandi.wav"]),
 ("voice_comm_stand_jap", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jap_hold.wav"]),
 ("voice_comm_stand_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_stand_jin", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_stand.mp3"]),
 ("voice_comm_stand_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_stand_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 ("voice_comm_stand_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 ("voice_comm_stand_tur2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 #Blunt weapon
 ("voice_comm_blunt_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["shiyongdunqi.wav"]),
 ("voice_comm_stand_jap", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jap_blunt.mp3"]),
 ("voice_comm_stand_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_stand_jin", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_blunt.mp3"]),
 ("voice_comm_stand_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_stand_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 ("voice_comm_stand_tur", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
 ("voice_comm_stand_tur2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []), 
  # battle cries.
 ("voice_cry_fem_brit", sf_priority_8|sf_vol_13, [
"ming_no_mercy.mp3",
"ming_catch_wokou.mp3"
 ]), 
 ("voice_cry_fem_fren", sf_priority_8|sf_vol_13, ["woman_shout_jap_01.wav", "woman_shout_jap_02.wav", "woman_shout_jap_03.wav", "woman_shout_jap_04.wav", "woman_shout_jap_05.wav", "woman_shout_jap_06.wav", "woman_shout_jap_07.wav"]),
 ("voice_cry_fem_prus", sf_priority_8|sf_vol_13, [
   "prus_f_battlecry_1.wav"
  ,"prus_f_battlecry_2.wav"
  ,"prus_f_battlecry_3.wav"
  ,"prus_f_battlecry_4.wav"
  ,"prus_f_battlecry_5.wav"
  ,"prus_f_battlecry_6.wav"
  ,"prus_f_battlecry_7.wav"
  ,"prus_f_battlecry_8.wav"
  ,"prus_f_battlecry_9.wav"
  ,"prus_f_battlecry_10.wav"
 ]),
 ("voice_cry_fem_russ", sf_priority_8|sf_vol_13, [
   "rus_f_battlecry1.wav"
  ,"rus_f_battlecry2.wav"
  ,"rus_f_battlecry3.wav"
  ,"rus_f_battlecry4.wav"
  ,"rus_f_battlecry5.wav"
  ,"rus_f_battlecry6.wav"
  ,"rus_f_battlecry7.wav"
  ,"rus_f_battlecry8.wav"
  ,"rus_f_battlecry9.wav"
 ]),
 ("voice_cry_fem_aust", sf_priority_8|sf_vol_13, [
   "jin_f_melee.mp3"
  ,"jin_f_charge.mp3"
  ,"jin_f_all_fire.mp3"
 ]),
 ("voice_cry_fem_russ_ukr", sf_priority_8|sf_vol_13, [
   "ukr_f_battlecry_1.wav"
  ,"ukr_f_battlecry_2.wav"
  ,"rus_f_battlecry1.wav"
  ,"rus_f_battlecry2.wav"
 ]),
 ("voice_cry_fem_rhen", sf_priority_8|sf_vol_13, [
   "rus_f_battlecry1.wav"
  ,"rus_f_battlecry2.wav"
  ,"rus_f_battlecry3.wav"
  ,"rus_f_battlecry4.wav"
  ,"rus_f_battlecry5.wav"
  ,"rus_f_battlecry6.wav"
  ,"rus_f_battlecry7.wav"
  ,"rus_f_battlecry8.wav"
  ,"rus_f_battlecry9.wav"
 ]),
 
 # Surrendering
 ("voice_surrender_fem_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["brit_f_surrender_1.wav","brit_f_surrender_2.wav","brit_f_surrender_3.wav","brit_f_surrender_4.wav","brit_f_surrender_5.wav"]),
 ("voice_surrender_fem_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["woman_shout_jap_needmedic_01.wav", "woman_shout_jap_needmedic_02.wav"]),
 ("voice_surrender_fem_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["prus_f_surrender_1.wav","prus_f_surrender_2.wav","prus_f_surrender_3.wav"]),
 ("voice_surrender_fem_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_surr.mp3"]),
 ("voice_surrender_fem_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ukr_f_surrender_1.wav","ukr_f_surrender_2.wav","ukr_f_surrender_3.wav","ukr_f_surrender_4.wav","ukr_f_surrender_5.wav","ukr_f_surrender_6.wav"]),
 
 # # Officer commands # #
 
 # Make Ready
 ("voice_comm_ready_fem_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["range_weapan_ming.mp3"]),
 ("voice_comm_ready_fem_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["french_f_ready_1.wav","french_f_ready_2.wav","french_f_ready_3.wav","french_f_ready_5.wav"]),
 ("voice_comm_ready_fem_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["prus_f_ready_1.wav","prus_f_ready_2.wav"]),
 ("voice_comm_ready_fem_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_at_my_command.mp3"]),
 ("voice_comm_ready_fem_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ukr_f_ready_1.wav","ukr_f_ready_2.wav","ukr_f_ready_3.wav"]),
 
 # Present
 ("voice_comm_present_fem_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["fire_at_command_ming.mp3","fire_at_command2_ming.mp3"]),
 ("voice_comm_present_fem_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["french_f_present_1.wav","french_f_present_2.wav","french_f_present_3.wav"]),
 ("voice_comm_present_fem_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["prus_f_present_1.wav","prus_f_present_2.wav"]),
 ("voice_comm_present_fem_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_range.mp3"]),
 ("voice_comm_present_fem_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ukr_f_present_1.wav","ukr_f_present_2.wav"]),
 
 # Fire
 ("voice_comm_fire_fem_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["fire2_all_ming.mp3"]),
 ("voice_comm_fire_fem_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["woman_shout_jap_fire_01.wav", "woman_shout_jap_fire_02.wav", "woman_shout_jap_fire_03.wav", "woman_shout_jap_fire_04.wav"]),
 ("voice_comm_fire_fem_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["prus_f_fire_1.wav","prus_f_fire_2.wav"]),
 ("voice_comm_fire_fem_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_all_fire.mp3"]),
 ("voice_comm_fire_fem_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ukr_f_fire_1.wav","ukr_f_fire_2.wav"]),
 
 # Fire left
 ("voice_comm_fire_fem_left_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["fire_left_ming.mp3"]),
 ("voice_comm_fire_fem_left_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["woman_shout_jap_fire_01.wav", "woman_shout_jap_fire_02.wav", "woman_shout_jap_fire_03.wav", "woman_shout_jap_fire_04.wav"]),
 ("voice_comm_fire_fem_left_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["prus_feuer1.wav","prus_feuer2.wav","prus_feuer3.wav"]),
 ("voice_comm_fire_fem_left_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_fire_left.mp3"]),
 ("voice_comm_fire_fem_left_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ukr_fire1.wav","ukr_fire2.wav"]),
 ("voice_comm_fire_fem_left_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_disparo.mp3","orden_disparo1.mp3","orden_disparo2.mp3","orden_disparo3.mp3"]),
 
 
 # Fire middle
 ("voice_comm_fire_fem_middle_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["fire_mid_ming.mp3"]),
 ("voice_comm_fire_fem_middle_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["woman_shout_jap_fire_01.wav", "woman_shout_jap_fire_02.wav", "woman_shout_jap_fire_03.wav", "woman_shout_jap_fire_04.wav"]),
 ("voice_comm_fire_fem_middle_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["prus_feuer1.wav","prus_feuer2.wav","prus_feuer3.wav"]),
 ("voice_comm_fire_fem_middle_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_fire_mid.mp3"]),
 ("voice_comm_fire_fem_middle_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ukr_fire1.wav","ukr_fire2.wav"]),
 ("voice_comm_fire_fem_middle_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_disparo.mp3","orden_disparo1.mp3","orden_disparo2.mp3","orden_disparo3.mp3"]),
 
 # Fire right
 ("voice_comm_fire_fem_right_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["fire_right_ming.mp3"]),
 ("voice_comm_fire_fem_right_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["woman_shout_jap_fire_01.wav", "woman_shout_jap_fire_02.wav", "woman_shout_jap_fire_03.wav", "woman_shout_jap_fire_04.wav"]),
 ("voice_comm_fire_fem_right_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["prus_feuer1.wav","prus_feuer2.wav","prus_feuer3.wav"]),
 ("voice_comm_fire_fem_right_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_fire_right.mp3"]),
 ("voice_comm_fire_fem_right_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ukr_fire1.wav","ukr_fire2.wav"]),
 ("voice_comm_fire_fem_right_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["orden_disparo.mp3","orden_disparo1.mp3","orden_disparo2.mp3","orden_disparo3.mp3"]),
 
 # Charge
 ("voice_comm_charge_fem_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["charge_ming.mp3"]),
 ("voice_comm_charge_fem_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["woman_shout_jap_charge_01.wav", "woman_shout_jap_charge_02.wav"]),
 ("voice_comm_charge_fem_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["prus_f_charge_1.wav","prus_f_charge_2.wav","prus_f_charge_3.wav","prus_f_charge_4.wav","prus_f_charge_5.wav"]),
 ("voice_comm_charge_fem_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_charge.mp3"]),
 ("voice_comm_charge_fem_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["rus_f_charge5.wav"]),
 
 # Company, advance!
 ("voice_comm_advance_fem_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["forward_ming.mp3"]),
 ("voice_comm_advance_fem_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["woman_shout_jap_advance_01.wav", "woman_shout_jap_advance_02.wav", "woman_shout_jap_advance_03.wav", "woman_shout_jap_advance_04.wav"]),
 ("voice_comm_advance_fem_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["prus_f_advance_1.wav","prus_f_advance_2.wav","prus_f_advance_3.wav"]),
 ("voice_comm_advance_fem_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_forward.mp3"]),
 ("voice_comm_advance_fem_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ukr_f_advance_1.wav","ukr_f_advance_2.wav","ukr_f_advance_3.wav","ukr_f_advance_4.wav","rus_f_advance1.wav","rus_f_advance2.wav"]),
 
 # Hold this position!
 ("voice_comm_hold_fem_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["hold_this_postion_ming.mp3","hold_this_postion2_ming.mp3"]),
 ("voice_comm_hold_fem_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["french_f_holdpos_1.wav","french_f_holdpos_2.wav","french_f_holdpos_3.wav","french_f_holdpos_4.wav"]),
 ("voice_comm_hold_fem_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["prus_f_holdpos_1.wav","prus_f_holdpos_2.wav","prus_f_holdpos_3.wav"]),
 ("voice_comm_hold_fem_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_hold.mp3"]),
 ("voice_comm_hold_fem_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ukr_f_holdpos_1.wav","ukr_f_holdpos_2.wav"]),
 
 # Fire at will!
 ("voice_comm_fire_at_will_fem_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["fire_at_will_ming.mp3"]),
 ("voice_comm_fire_at_will_fem_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["woman_shout_jap_fire_01.wav", "woman_shout_jap_fire_02.wav", "woman_shout_jap_fire_03.wav"]),
 ("voice_comm_fire_at_will_fem_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["prus_f_fireatwill_1.wav","prus_f_fireatwill_2.wav","prus_f_fireatwill_3.wav"]),
 ("voice_comm_fire_at_will_fem_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_fire_at_will2.mp3"]),
 ("voice_comm_fire_at_will_fem_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ukr_f_fireatwill_1.wav","ukr_f_fireatwill_2.wav"]),
 
 # Company, on me! 
 ("voice_comm_on_me_fem_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["follow_ming.mp3"]),
 ("voice_comm_on_me_fem_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["woman_shout_jap_onme_01.wav", "woman_shout_jap_onme_02.wav"]),
 ("voice_comm_on_me_fem_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["prus_f_onme_1.wav","prus_f_onme_2.wav"]),
 ("voice_comm_on_me_fem_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jim_f_follow.mp3"]),
 ("voice_comm_on_me_fem_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ukr_f_onme_1.wav","ukr_f_onme_2.wav"]),
 
 # Fall back!
 ("voice_comm_fall_back_fem_brit", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["retreat2_ming.mp3","retreat_ming.mp3"]),
 ("voice_comm_fall_back_fem_fren", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["woman_shout_jap_retreat_01.wav", "woman_shout_jap_retreat_02.wav", "woman_shout_jap_retreat_03.wav", "woman_shout_jap_retreat_04.wav"]),
 ("voice_comm_fall_back_fem_prus", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["prus_f_retreat_1.wav","prus_f_retreat_2.wav"]),
 ("voice_comm_fall_back_fem_russ", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_retreat.mp3","jin_f_retreat2.mp3"]),
 ("voice_comm_fall_back_fem_ukra", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ukr_f_retreat_1.wav","ukr_f_retreat_2.wav","ukr_f_retreat_3.wav","ukr_f_retreat_4.wav","ukr_f_retreat_5.wav","ukr_f_retreat_6.wav"]),
 
 #Mount
 ("voice_comm_fall_fem_mount_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["mount_ming.mp3"]),
 ("voice_comm_fall_fem_mount_ming1", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_fem_mount_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 ("voice_comm_fall_fem_mount_ming3", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_mount.mp3"]),
 ("voice_comm_fall_fem_mount_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_mount.mp3"]),
 ("voice_comm_fall_fem_mount_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, []),
 
 #Dismount
 ("voice_comm_fall_fem_dismount_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["dismount_ming.mp3"]),
 ("voice_comm_fall_fem_dismount_ming1", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_fall_fem_dismount_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_fall_fem_dismount_ming3", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_dismount.mp3"]),
 ("voice_comm_fall_fem_dismount_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_dismount.mp3"]),
 ("voice_comm_fall_fem_dismount_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 
 #Stand closer
 ("voice_comm_fall_fem_closer_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["stand_closer_ming.mp3","stand_closer2_ming.mp3"]),
 ("voice_comm_fall_fem_closer_ming1", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_fall_fem_closer_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_fall_fem_closer_ming3", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_close.mp3"]),
 ("voice_comm_fall_fem_closer_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_close.mp3"]),
 ("voice_comm_fall_fem_closer_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 
 #Spread
 ("voice_comm_fall_fem_spread_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["spread_out_ming.mp3","spread_out2_ming.mp3"]),
 ("voice_comm_fall_fem_spread_ming1", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["stand_closer_ming.mp3","stand_closer2_ming.mp3"]),
 ("voice_comm_fall_fem_spread_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_fall_fem_spread_ming3", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_spread.mp3"]),
 ("voice_comm_fall_fem_spread_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_spread.mp3"]),
 ("voice_comm_fall_fem_spread_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 
 #Use any weapon
 ("voice_comm_fall_fem_any_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["all_weapon_ming.mp3","all_weapon_ming2.mp3"]),
 ("voice_comm_fall_fem_any_ming1", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["stand_closer_ming.mp3","stand_closer2_ming.mp3"]),
 ("voice_comm_fall_fem_any_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_fall_fem_any_ming3", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_any.mp3"]),
 ("voice_comm_fall_fem_any_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_any.mp3"]),
 ("voice_comm_fall_fem_any_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),

 #1 row
 ("voice_comm_fall_fem_1_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["one_row_ming.mp3"]),
 ("voice_comm_fall_fem_1_ming1", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["stand_closer_ming.mp3","stand_closer2_ming.mp3"]),
 ("voice_comm_fall_fem_1_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_fall_fem_1_ming3", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_1row.mp3"]),
 ("voice_comm_fall_fem_1_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_1row.mp3"]),
 ("voice_comm_fall_fem_1_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]), 
 
 #2 row
 ("voice_comm_fall_fem_2_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["two_row_ming.mp3"]),
 ("voice_comm_fall_fem_2_ming1", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["stand_closer_ming.mp3","stand_closer2_ming.mp3"]),
 ("voice_comm_fall_fem_2_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_fall_fem_2_ming3", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_2row.mp3"]),
 ("voice_comm_fall_fem_2_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_fall_fem_2_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]), 
 
 #3 row
 ("voice_comm_fall_fem_3_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["three_row_ming.mp3"]),
 ("voice_comm_fall_fem_3_ming1", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["stand_closer_ming.mp3","stand_closer2_ming.mp3"]),
 ("voice_comm_fall_fem_3_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_fall_fem_3_ming3", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_3row.mp3"]),
 ("voice_comm_fall_fem_3_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_fall_fem_3_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]), 
 
 #4 row
 ("voice_comm_fall_fem_4_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["four_row_ming.mp3"]),
 ("voice_comm_fall_fem_4_ming1", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["stand_closer_ming.mp3","stand_closer2_ming.mp3"]),
 ("voice_comm_fall_fem_4_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_fall_fem_4_ming3", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_4row.mp3"]),
 ("voice_comm_fall_fem_4_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_fall_fem_4_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]), 
 
 #5 row
 ("voice_comm_fall_fem_5_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["five_row_ming.mp3"]),
 ("voice_comm_fall_fem_5_ming1", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["stand_closer_ming.mp3","stand_closer2_ming.mp3"]),
 ("voice_comm_fall_fem_5_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_fall_fem_5_ming3", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_5row.mp3"]),
 ("voice_comm_fall_fem_5_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_fall_fem_5_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]), 
 
 #Hold fire
 ("voice_comm_fall_fem_hold_fire_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["fire_at_command_ming.mp3","fire_at_command_ming2.mp3"]),
 ("voice_comm_fall_fem_hold_fire_ming1", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["stand_closer_ming.mp3","stand_closer2_ming.mp3"]),
 ("voice_comm_fall_fem_hold_fire_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_fall_fem_hold_fire_ming3", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_hold_fire.mp3"]),
 ("voice_comm_fall_fem_hold_fire_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_fall_fem_hold_fire_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),  
 
 #Melee
 ("voice_comm_fall_fem_melee_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["melee_ming.mp3","melee2_ming.mp3"]),
 ("voice_comm_fall_fem_melee_ming1", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["stand_closer_ming.mp3","stand_closer2_ming.mp3"]),
 ("voice_comm_fall_fem_melee_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_fall_fem_melee_ming3", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_melee.mp3"]),
 ("voice_comm_fall_fem_melee_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_fall_fem_melee_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),  
 
 #Range weapon
 ("voice_comm_fall_fem_range_weapon_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["range_weapan_ming.mp3"]),
 ("voice_comm_fall_fem_range_weapon_ming1", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["stand_closer_ming.mp3","stand_closer2_ming.mp3"]),
 ("voice_comm_fall_fem_range_weapon_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_fall_fem_range_weapon_ming3", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_range.mp3"]),
 ("voice_comm_fall_fem_range_weapon_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_fall_fem_range_weapon_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]), 
 
 #Retreat
 ("voice_comm_fall_fem_retreat_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["retreat_ming.mp3","retreat2_ming.mp3"]),
 ("voice_comm_fall_fem_retreat_ming1", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["stand_closer_ming.mp3","stand_closer2_ming.mp3"]),
 ("voice_comm_fall_fem_retreat_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_fall_fem_retreat_ming3", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_retreat.mp3","jin_f_retreat2.mp3"]),
 ("voice_comm_fall_fem_retreat_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_fall_fem_retreat_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]), 
 
  #Blunt weapon
 ("voice_comm_blunt_fem_ming", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_catch_wokou.mp3"]),
 ("voice_comm_stand_ming1", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["stand_closer_ming.mp3","stand_closer2_ming.mp3"]),
 ("voice_comm_stand_ming2", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_stand_ming3", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["jin_f_blunt.mp3"]),
 ("voice_comm_stand_ming4", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]),
 ("voice_comm_stand_spa", sf_priority_8|sf_vol_13|sf_stream_from_hd, ["ming_mount.mp3"]), 
 
 # Muscician sounds
 #DRUM
 #British
 ("drum_britain_1",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["brit_britishgrenadiers.ogg"]),
 ("drum_britain_2",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["brit_girlileftbehindme.ogg"]),
 ("drum_britain_3",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["brit_lili.ogg"]),
 ("drum_britain_4",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["brit_menofharlech.ogg"]),
 ("drum_britain_5",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["brit_rulebritannia.ogg"]),
 #French
 ("drum_france_1",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["french_drum_aux_champs.ogg"]),
 ("drum_france_2",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["fren_lacharge.ogg"]),
 ("drum_france_3",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["fren_diane.ogg"]),
 ("drum_france_4",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["fren_grenadiere.ogg"]),
 ("drum_france_5",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["fren_lapascadence.ogg"]),
 #Prussian
 ("drum_prussia_1",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["prus_yorkscher.ogg"]),
# ("drum_prussia_2",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["prus_dessauer.ogg"]),
 ("drum_prussia_3",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["prussian_drum_hohenfriedberger.ogg"]),
 ("drum_prussia_4",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["prussian_drum_lockmarsch.ogg"]),
 ("drum_prussia_5",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["prussian_drum_parademarsch.ogg"]),
 ("drum_prussia_6",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["prussian_drum_praesentiermarsch.ogg"]),
 #Russian
("drum_russia_1",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["russian_drum_grenadiers.ogg"]),
("drum_russia_2",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["russian_drum_izmailovsky.ogg"]),
("drum_russia_3",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["russian_drum_march_of_attacking.ogg"]),
("drum_russia_4",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["russian_drum_preabrazhensky.ogg"]),
("drum_russia_5",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["russian_drum_semenovsky.ogg"]),
 #Austrian
("drum_austria_1",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["austrian_drum_grenadiersmarsch.ogg"]),
("drum_austria_2",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["austrian_drum_koburg.ogg"]),
("drum_austria_3",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["austrian_drum_pappenheimer.ogg"]),
("drum_austria_4",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["austrian_drum_pariser_einzugsmarsch.ogg"]),
("drum_austria_5",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["austrian_drum_prinz_von_eugen.ogg"]),
 #Highland
("drum_highland_1",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["british_drum_blue_bonnets.ogg"]),
("drum_highland_2",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["british_drum_bonnie_dundee.ogg"]),
 #Signals
("drum_signal_1",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["drum_signal_camp_taps.ogg"]),
("drum_signal_2",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["drum_signal_cease_fire.ogg"]),
("drum_signal_3",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["drum_signal_drummers_call.ogg"]),
 
 #FIFE
 #British
 ("fife_britain_1",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["british_fife_british_grenadiers.ogg"]),
 ("fife_britain_2",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["british_fife_girl_i_left_behind.ogg"]),
 ("fife_britain_3",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["british_fife_lilliburlero.ogg"]),
 ("fife_britain_4",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["british_fife_men_of_harlech.ogg"]),
 ("fife_britain_5",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["british_fife_rule_brit.ogg"]),
 #French
 ("fife_france_1",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["french_fife_aux_champs.ogg"]),
 ("fife_france_2",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["french_fife_la_charge.ogg"]),
 ("fife_france_3",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["french_fife_la_diane.ogg"]),
 ("fife_france_4",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["french_fife_la_grenadiere.ogg"]),
 ("fife_france_5",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["french_fife_la_pa_cadence.ogg"]),
 #Prussian
 ("fife_prussia_1",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["prussian_fife_yorckscher.ogg"]), 
 ("fife_prussia_2",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["prussian_fife_hohenfriedeberger.ogg"]),
 ("fife_prussia_3",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["prussian_fife_lockmarsch.ogg"]),
 ("fife_prussia_4",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["prussian_fife_parademarsch_der_spielleute.ogg"]),
 ("fife_prussia_5",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["prussian_fife_praesentiermarsch.ogg"]),
 #Russian
 ("fife_russia_1",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["russian_fife_grenadiers_march.ogg"]),
 ("fife_russia_2",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["russian_fife_izmailovsky.ogg"]),
 ("fife_russia_3",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["russian_fife_of_attacking.ogg"]),
 ("fife_russia_4",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["russian_fife_preobrazhensky.ogg"]),
 ("fife_russia_5",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["russian_fife_semenovsky.ogg"]),
 #Austrian
 ("fife_austria_1",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["austrian_fife_grenadiermarsch.ogg"]),
 ("fife_austria_2",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["austrian_fife_derkoburger.ogg"]),
 ("fife_austria_3",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["austrian_fife_pappenheimer.ogg"]),
 ("fife_austria_4",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["austrian_fife_pariser.ogg"]),
 ("fife_austria_5",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["austrian_fife_prinzeugen.ogg"]),

 #BUGLE
 #British
 ("bugle_britain_1",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["bugle_british_boots.ogg"]),
 ("bugle_britain_2",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["british_light_inf.ogg"]),
 #French
 ("bugle_france_1",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["bugle_french_danslehussards.ogg"]),
 ("bugle_france_2",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["bugle_french_lamarche.ogg"]),
 #Prussian
 ("bugle_prussia_1",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["bugle_prussian_althessischer.ogg"]),
 ("bugle_prussia_2",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["bugle_prussian_fehrbell.ogg"]),
 ("bugle_prussia_3",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["bugle_prussian_freiwilligen.ogg"]),
 #Russian
 ("bugle_russia_1",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["bugle_russian_marchartillery.ogg"]),
 ("bugle_russia_2",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["bugle_russian_jaegers.ogg"]),
 ("bugle_russia_3",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["bugle_russian_musketeers.ogg"]),
 #Austrian
 ("bugle_austria_1",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["bugle_austrian_leban.ogg"]),
 ("bugle_austria_2",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["bugle_austrian_strauch.ogg"]),
 #Signals
 ("bugle_signal_1",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["bugle_call_assamble.ogg"]),
 ("bugle_signal_2",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["bugle_call_extend.ogg"]),
 ("bugle_signal_3",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["bugle_call_closeranks.ogg"]),
 ("bugle_signal_4",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["bugle_call_ondiscenemy.ogg"]),
 ("bugle_signal_5",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["bugle_call_fire.ogg"]),

 #BAGPIPES
 #Highland
 ("bagpipes_britain_1",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["bluebonnets.ogg"]),
 ("bagpipes_britain_2",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["bonniedundee.ogg"]),
 #Additional...
 ("bagpipes_extra_1",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["blackbear.ogg"]),
 ("bagpipes_extra_2",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["amazing.ogg"]),
 ("bagpipes_extra_3",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["balmoral.ogg"]),
 ("bagpipes_extra_4",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["bonniedundee.ogg"]),
 ("bagpipes_extra_5",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["cockothenorth.ogg"]),
 ("bagpipes_extra_6",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["highlandcathedral.ogg"]),
 ("bagpipes_extra_7",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["myhome.ogg"]),
 ("bagpipes_extra_8",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["scotlandthebrave.ogg"]),
 ("bagpipes_extra_9",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["skyeboatsong.ogg"]),

 #PIANO
 ("piano_loop_1",sf_priority_15|sf_vol_12|sf_stream_from_hd|sf_always_send_via_network, ["piano_beethoven_fur_elise.ogg"]),
 ("piano_loop_2",sf_priority_15|sf_vol_12|sf_stream_from_hd|sf_always_send_via_network, ["piano_beethoven_ecossaise.ogg"]),
 ("piano_loop_3",sf_priority_15|sf_vol_12|sf_stream_from_hd|sf_always_send_via_network, ["piano_erik_satie_gymnopedie_3.ogg"]),
 ("piano_loop_4",sf_priority_15|sf_vol_12|sf_stream_from_hd|sf_always_send_via_network, ["piano_beethoven_laendler.ogg"]),
 ("piano_loop_5",sf_priority_15|sf_vol_12|sf_stream_from_hd|sf_always_send_via_network, ["piano_lift_motif.ogg"]),
 ("piano_loop_6",sf_priority_15|sf_vol_12|sf_stream_from_hd|sf_always_send_via_network, ["piano_bach_prelude.ogg"]),
 ("piano_loop_7",sf_priority_15|sf_vol_12|sf_stream_from_hd|sf_always_send_via_network, ["piano_wagner_bridal_chorus.ogg"]),
 ("piano_loop_8",sf_priority_15|sf_vol_12|sf_stream_from_hd|sf_always_send_via_network, ["piano_schubert_ave_maria.ogg"]),
 
 #ORGAN
 ("organ_loop_1",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["organ_bach_toccata_and_fugue.ogg"]),
 ("organ_loop_2",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["organ_bach_toccata_and_fugue_2.ogg"]),
 ("organ_loop_3",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["organ_bach_prelude_and_fugue.ogg"]),
 ("organ_loop_4",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["organ_buxtehude_prelude.ogg"]),
 ("organ_loop_5",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["organ_tiny_fugue.ogg"]),
 ("organ_loop_6",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["organ_wagner_bridal_chorus.ogg"]),
 ("organ_loop_7",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["organ_bach_chromatic_fuge.ogg"]),
 ("organ_loop_8",sf_priority_15|sf_vol_15|sf_stream_from_hd|sf_always_send_via_network, ["organ_bach_chromatic_fantasia.ogg"]),
 
 ("instruments_end",0, []),
 
 # tutorial
 ("tutorial_voice_start_1",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_1.ogg"]),
 #("tutorial_voice_start_2",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_2.ogg"]),
 #("tutorial_voice_start_3",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_3.ogg"]),
 ("tutorial_voice_1",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_4.ogg"]),
 ("tutorial_voice_2",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_5.ogg"]),
 ("tutorial_voice_3",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_6.ogg"]),
 #("tutorial_voice_4",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_7.ogg"]),
 ("tutorial_voice_4",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_8.ogg"]),
 ("tutorial_voice_5",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_9.ogg"]),
 ("tutorial_voice_6",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_10.ogg"]),
 ("tutorial_voice_7",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_11.ogg"]),
 ("tutorial_voice_8",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_12.ogg"]),
 ("tutorial_voice_9",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_13.ogg"]),
 ("tutorial_voice_10",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_14.ogg"]),
 ("tutorial_voice_11",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_15.ogg"]),
 ("tutorial_voice_12",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_16.ogg"]),
 ("tutorial_voice_13",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_17.ogg"]),
 ("tutorial_voice_14",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_18.ogg"]),
 ("tutorial_voice_15",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_19.ogg"]),
 ("tutorial_voice_16",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_20.ogg"]),
 ("tutorial_voice_17",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_21.ogg"]),
 ("tutorial_voice_18",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_22.ogg"]),
 ("tutorial_voice_19",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_23.ogg"]),
 ("tutorial_voice_20",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_24.ogg"]),
 ("tutorial_voice_21",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_25.ogg"]),
 ("tutorial_voice_22",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_26.ogg"]),
 ("tutorial_voice_23",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_27.ogg"]),
 ("tutorial_voice_24",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_28.ogg"]),
 ("tutorial_voice_25",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_29.ogg"]),
 ("tutorial_voice_26",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["tutorial_voice_30.ogg"]),
 
 
 # SP narrators 
 ("mission_narrator_1",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["mission_narrator_1.wav"]),
 ("mission_narrator_2",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["mission_narrator_1.wav"]),
 ("mission_narrator_3",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["mission_narrator_1.wav"]),
 ("mission_narrator_4",sf_2d|sf_priority_10|sf_vol_15|sf_stream_from_hd, ["mission_narrator_1.wav"]),
 
 # v15 
 ("cannonball_hit_on_water",sf_vol_6, ["dedal_cannonball_hit_water.ogg"]),
 ("missile_hit_on_water",sf_vol_4, ["dedal_missile_hit_water_1.ogg", "hit_water_new15.ogg", "hit_water_new15_1.ogg"]),

 ("musket_medium_range", sf_2d|sf_priority_10|sf_vol_2,[
 "dedal_musket_far_1.ogg",
 "dedal_musket_far_2.ogg",
 "dedal_musket_far_3.ogg",
 "dedal_musket_far_4.ogg",
 "dedal_musket_far_5.wav"
 ]),
 ("musket_far_range", sf_2d|sf_priority_10|sf_vol_3,["dedal_musket_far_1.ogg", "dedal_musket_far_2.ogg", "dedal_musket_far_3.ogg", "dedal_musket_far_4.ogg"]),
	("shield_taunt", sf_priority_8|sf_vol_5,["shield_taunt.wav"]),
    
("whistle", sf_vol_7, ["whistle1.ogg", "whistle2.ogg"]),

("tc_fangun", sf_2d, ["tc_fangun.mp3"]),

("tc_fangun2", sf_2d, ["rolling_armored.mp3"]),

("qisi", sf_vol_7, ["qisi.mp3"]),

("wuqiang", sf_vol_7, ["wuqiang.mp3"]),

 ("sounds_end",0, []),
]
