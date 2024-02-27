from header_music import *
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory

tracks = [
##  ("losing_battle", "alosingbattle.mp3", sit_calm|sit_action),
##  ("reluctant_hero", "reluctanthero.mp3", sit_action),
##  ("the_great_hall", "thegreathall.mp3", sit_calm),
##  ("requiem", "requiem.mp3", sit_calm),
##  ("silent_intruder", "silentintruder.mp3", sit_calm|sit_action),
##  ("the_pilgrimage", "thepilgrimage.mp3", sit_calm),
##  ("ambushed", "ambushed.mp3", sit_action),
##  ("triumph", "triumph.mp3", sit_action),

##  ("losing_battle", "alosingbattle.mp3", mtf_sit_map_travel|mtf_sit_attack),
##  ("reluctant_hero", "reluctanthero.mp3", mtf_sit_attack),
##  ("the_great_hall", "thegreathall.mp3", mtf_sit_map_travel),
##  ("requiem", "requiem.mp3", mtf_sit_map_travel),
##  ("silent_intruder", "silentintruder.mp3", mtf_sit_map_travel|mtf_sit_attack),
##  ("the_pilgrimage", "thepilgrimage.mp3", mtf_sit_map_travel),
##  ("ambushed", "ambushed.mp3", mtf_sit_attack),
##  ("triumph", "triumph.mp3", mtf_sit_attack),
  ("bogus", "cant_find_this.ogg", 0, 0),
  ("mount_and_blade_title_screen", "main.ogg", mtf_module_track|mtf_sit_main_title|mtf_start_immediately, 0),

  ("first_rain_of_lin_an", "first_rain_of_lin_an.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("three_kingdom_liangzhou", "three_kingdom_liangzhou.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("Against the World", "against_the_world.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("loch_lomond", "loch_lomond.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("wave_of_sunrise", "wave_of_sunrise.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("triumph", "triumph.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("when_the_spring_comes", "when_the_spring_comes.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("when_all_kingdoms_fall", "when_all_kingdoms_fall.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("he_is_a_pirate", "he_is_a_pirate.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("taichi", "taichi.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("elgar_pomp_and_circumstance_march_1", "elgar_pomp_and_circumstance_march_1.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("youths_travel", "youths_travel.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("weapons_of_imprial_guard", "weapons_of_imprial_guard.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("king_of_the_world", "king_of_the_world.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("sword_of_the_stranger", "sword_of_the_stranger.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("mazurek_dabrowskiego_polish_national_anthem", "mazurek_dabrowskiego_polish_national_anthem.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("mooncake", "mooncake.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("qi_army_song", "qi_army_song.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("novera", "novera.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("rising_sun", "rising_sun.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("dusk_to_dawn", "dusk_to_dawn.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("palace_memories", "palace_memories.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("kirin", "kirin.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("sakura", "sakura.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("shogun2", "shogun2.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("imperial_match", "imperial_match.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("three_kingdoms", "three_kingdoms.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("hej_sokoly", "hej_sokoly.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("battle_against_a_true_hero_orchestral", "menu_battle_against_a_true_hero_orchestral_by_hellkite_drake.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("hopes_and_dreams_orchestral_by_hellkite_drake", "menu_hopes_and_dreams_orchestral_by_hellkite_drake.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("spear_of_justice", "menu_spear_of_justice_orchestral_by_malcolm_robinson.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("bozhe-tsarya_khrani", "bozhe-tsarya_khrani.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("pilgrimage", "main2.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("wujiang", "wujiang.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("arisen", "main3.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("chunfengting", "chunfengting.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("apocalypse", "apocalypse.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("fightwithgod.mp3", "fightwithgod.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("vivaldi_concerto_flute_violin_continuo_allegro", "vivaldi_concerto_flute_violin_continuo_allegro.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("vivaldi_concerto_grosso_8_allegro", "vivaldi_concerto_grosso_8_allegro.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("mendelssohn_wedding_march_recessional", "mendelssohn_wedding_march_recessional.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("bach_brandenburg_concerto_movement_1", "bach_brandenburg_concerto_movement_1.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("pachelbel_canon", "pachelbel_canon.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("saint_saens_danse_macabre", "saint_saens_danse_macabre.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("rossini_william_tell_overture", "rossini_william_tell_overture.ogg", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  
  #v15
  ("first_french_empire", "first_french_empire.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("god_save_the_king", "god_save_the_king.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("gott_erhalte_franz_den_kaiser", "Gott_erhalte_Franz_den_Kaiser.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("let_the_thunder_of_victory_rumble", "let_the_thunder_of_victory_rumble.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("march_of_the_preobrazhensky_regiment", "March_of_the_Preobrazhensky_Regiment.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),
  ("the_british_grenadier_march", "The_British_Grenadiers_march.mp3", mtf_module_track|mtf_sit_fight|mtf_sit_multiplayer_fight|mtf_sit_ambushed|mtf_sit_siege, 0),

  ("track_end", "track_end.ogg", 0, 0),
]
