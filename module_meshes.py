from header_meshes import *

####################################################################################################################
#  Each mesh record contains the following fields:
#  1) Mesh id: used for referencing meshes in other files. The prefix mesh_ is automatically added before each mesh id.
#  2) Mesh flags. See header_meshes.py for a list of available flags
#  3) Mesh resource name: Resource name of the mesh
#  4) Mesh translation on x axis: Will be done automatically when the mesh is loaded
#  5) Mesh translation on y axis: Will be done automatically when the mesh is loaded
#  6) Mesh translation on z axis: Will be done automatically when the mesh is loaded
#  7) Mesh rotation angle over x axis: Will be done automatically when the mesh is loaded
#  8) Mesh rotation angle over y axis: Will be done automatically when the mesh is loaded
#  9) Mesh rotation angle over z axis: Will be done automatically when the mesh is loaded
#  10) Mesh x scale: Will be done automatically when the mesh is loaded
#  11) Mesh y scale: Will be done automatically when the mesh is loaded
#  12) Mesh z scale: Will be done automatically when the mesh is loaded
####################################################################################################################

meshes = [
  ("meshes_begin", 0, "empty_mesh", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  
  ("mp_score_a", 0, "mp_score_a", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_score_b", 0, "mp_score_b", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("load_window", 0, "load_window", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("checkbox_off", render_order_plus_1, "checkbox_off", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("checkbox_on", render_order_plus_1, "checkbox_on", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("white_plane", 0, "white_plane", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("white_dot", 0, "white_dot", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("player_dot", 0, "player_dot", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_infantry", 0, "empty_mesh", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_archers", 0, "empty_mesh", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_cavalry", 0, "empty_mesh", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("inv_slot", 0, "inv_slot", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ingame_menu", 0, "mp_ingame_menu", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_left", 0, "mp_inventory_left", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_right", 0, "mp_inventory_right", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_choose", 0, "mp_inventory_choose", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_glove", 0, "mp_inventory_slot_glove", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_horse", 0, "mp_inventory_slot_horse", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_armor", 0, "mp_inventory_slot_armor", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_helmet", 0, "mp_inventory_slot_helmet", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_boot", 0, "mp_inventory_slot_boot", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_empty", 0, "mp_inventory_slot_empty", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_slot_equip", 0, "mp_inventory_slot_equip", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_left_arrow", 0, "mp_inventory_left_arrow", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_inventory_right_arrow", 0, "mp_inventory_right_arrow", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_host_main", 0, "mp_ui_host_main", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("mp_ui_command_panel", 0, "mp_ui_command_panel", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_command_border_l", 0, "mp_ui_command_border_l", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_command_border_r", 0, "mp_ui_command_border_r", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mp_ui_welcome_panel", 0, "mp_ui_welcome_panel", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("flag_project_sw", 0, "flag_project_britain", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_vg", 0, "flag_project_france", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_kh", 0, "flag_project_prussia", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_nd", 0, "flag_project_russia", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_rh", 0, "flag_project_austria", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_sr", 0, "flag_project_rhine", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_pl", 0, "blq3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("flag_projects_end", 0, "empty_mesh", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("flag_project_sw_miss", 0, "flag_project_britain", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_vg_miss", 0, "flag_project_france", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_kh_miss", 0, "flag_project_prussia", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_nd_miss", 0, "flag_project_russia", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_rh_miss", 0, "flag_project_austria", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_sr_miss", 0, "flag_project_russia", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_pl_miss", 0, "blq3", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("flag_project_misses_end", 0, "empty_mesh", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("banner_a01", 0, "banner1", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a02", 0, "banner2", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a03", 0, "banner3", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a04", 0, "banner4", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a05", 0, "banner5", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a06", 0, "banner6", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a07", 0, "banner7", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a08", 0, "banner8", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a09", 0, "banner9", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a10", 0, "banner10", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a11", 0, "banner11", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a12", 0, "banner12", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a13", 0, "banner13", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a14", 0, "banner14", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a15", 0, "banner15", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a16", 0, "banner16", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a17", 0, "banner17", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a18", 0, "banner18", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a19", 0, "banner19", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a20", 0, "banner20", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_a21", 0, "banner21", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b01", 0, "banner22", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b02", 0, "banner23", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b03", 0, "banner24", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b04", 0, "banner25", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b05", 0, "banner26", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b06", 0, "banner27", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b07", 0, "banner28", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b08", 0, "banner29", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b09", 0, "banner30", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b10", 0, "banner31", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b11", 0, "banner32", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b12", 0, "banner33", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b13", 0, "banner34", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b14", 0, "banner35", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b15", 0, "banner36", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b16", 0, "banner37", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b17", 0, "banner38", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b18", 0, "banner39", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b19", 0, "banner40", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b20", 0, "banner41", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_b21", 0, "banner42", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c01", 0, "banner43", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c02", 0, "banner44", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c03", 0, "banner45", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c04", 0, "banner46", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c05", 0, "banner47", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c06", 0, "banner48", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c07", 0, "banner49", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c08", 0, "banner50", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c09", 0, "banner51", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c10", 0, "banner52", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c11", 0, "banner53", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c12", 0, "banner54", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c13", 0, "banner55", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c14", 0, "banner56", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c15", 0, "banner57", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c16", 0, "banner58", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c17", 0, "banner59", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c18", 0, "banner60", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c19", 0, "banner61", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c20", 0, "banner62", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_c21", 0, "banner63", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d01", 0, "banner64", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d02", 0, "banner65", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d03", 0, "banner66", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d04", 0, "banner67", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d05", 0, "banner68", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d06", 0, "banner69", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d07", 0, "banner70", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d08", 0, "banner71", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d09", 0, "banner72", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d10", 0, "banner73", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d11", 0, "banner74", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d12", 0, "banner75", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d13", 0, "banner76", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d14", 0, "banner77", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d15", 0, "banner78", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d16", 0, "banner79", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d17", 0, "banner80", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d18", 0, "banner81", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d19", 0, "banner82", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d20", 0, "banner83", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_d21", 0, "banner84", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e01", 0, "banner85", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e02", 0, "banner86", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e03", 0, "banner87", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e04", 0, "banner88", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e05", 0, "banner89", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e06", 0, "banner90", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e07", 0, "banner91", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_e08", 0, "banner92", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  ("banner_kingdom_a", 0, "banner2", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_kingdom_b", 0, "banner5", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_kingdom_c", 0, "banner3", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_kingdom_d", 0, "banner1", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_kingdom_e", 0, "banner75", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_kingdom_f", 0, "banner4", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_kingdom_g", 0, "blqz", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banner_f21", 0, "empty_mesh", 0, 0, 0, -90, 0, 0, 1, 1, 1),

  
  ("banners_default_a", 0, "banner2", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_b", 0, "banner5", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_c", 0, "banner3", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_d", 0, "banner1", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_e", 0, "banner4", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  ("banners_default_f", 0, "banner75", 0, 0, 0, -90, 0, 0, 1, 1, 1),
  
  ("troop_label_banner",  0, "troop_label_banner", 0, 0, 0, 0, 0, 0, 10, 10, 10),

  ("ui_kingdom_shield_1", 0, "ui_kingdom_shield_a", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_kingdom_shield_2", 0, "ui_kingdom_shield_c", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_kingdom_shield_3", 0, "ui_kingdom_shield_g", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_kingdom_shield_4", 0, "ui_kingdom_shield_d", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_kingdom_shield_5", 0, "ui_kingdom_shield_h", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_kingdom_shield_6", 0, "ui_kingdom_shield_b", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_kingdom_shield_8", 0, "blq2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  #("flag_swadian", 0, "banner_a01", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("flag_vaegir", 0, "banner_a02", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("flag_khergit", 0, "banner_d01", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("flag_nord", 0, "banner_a03", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  #("flag_rhodok", 0, "banner_a04", 0, 0, 0, 0, 0, 0, 1, 1, 1),  

  ("mouse_arrow_down", 0, "mouse_arrow_down", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mouse_arrow_right", 0, "mouse_arrow_right", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mouse_arrow_left", 0, "mouse_arrow_left", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mouse_arrow_up", 0, "mouse_arrow_up", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mouse_arrow_plus", 0, "mouse_arrow_plus", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mouse_left_click", 0, "mouse_left_click", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mouse_right_click", 0, "mouse_right_click", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("main_menu_background", 0, "main_menu_nord", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("loading_background", 0, "load_screen_2", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("white_bg_plane_a", 0, "white_bg_plane_a", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_main", 0, "cb_ui_main", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_french_farm", 0, "cb_ui_maps_scene_french_farm", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_landshut", 0, "cb_ui_maps_scene_landshut", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_river_crossing", 0, "cb_ui_maps_scene_river_crossing", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_spanish_village", 0, "cb_ui_maps_scene_spanish_village", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_strangefields", 0, "cb_ui_maps_scene_strangefields", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_01", 0, "cb_ui_maps_scene_01", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_02", 0, "cb_ui_maps_scene_02", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_03", 0, "cb_ui_maps_scene_03", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_04", 0, "cb_ui_maps_scene_04", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_05", 0, "cb_ui_maps_scene_05", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_06", 0, "cb_ui_maps_scene_06", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_07", 0, "cb_ui_maps_scene_07", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_08", 0, "cb_ui_maps_scene_08", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("cb_ui_maps_scene_09", 0, "cb_ui_maps_scene_09", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("ui_kingdom_shield_7", 0, "ui_kingdom_shield_reb", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  ("flag_project_rb", 0, "flag_project_rebel", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("flag_project_rb_miss", 0, "flag_project_rebel", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  
  #MM
  ("ui_kingdom_shield_neutral", 0, "ui_kingdom_shield_neutral", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  
  ("ui_team_select_shield_aus", 0, "NewUIShieldsMM_Austria", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_team_select_shield_bri", 0, "NewUIShieldsMM_Britain", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_team_select_shield_fra", 0, "NewUIShieldsMM_France", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_team_select_shield_pru", 0, "NewUIShieldsMM_Prussia", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_team_select_shield_rus", 0, "NewUIShieldsMM_Russia", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_team_select_shield_rhi", 0, "NewUIShieldsMM_Rhine", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_team_select_shield_pol", 0, "QI", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_team_select_shield_reb", 0, "NewUIShieldsMM_Rebel", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("ui_team_select_shield_neu", 0, "NewUIShieldsMM_Neutral", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  
  #Construct props stuff
  ("construct_mesh_stakes", 0, "ui_construct_cdf", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("construct_mesh_stakes2", 0, "ui_construct_stakes", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("construct_mesh_sandbags", 0, "ui_construct_bags", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("construct_mesh_cdf_tri", 0, "ui_construct_cdf_tri", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("construct_mesh_gabion", 0, "ui_construct_gabion", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("construct_mesh_fence", 0, "ui_construct_fence", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("construct_mesh_plank", 0, "ui_construct_plank", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("construct_mesh_earthwork", 0, "ui_construct_dig", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("construct_mesh_explosives", 0, "ui_construct_crate", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  
  #Bonus icons
  ("bonus_icon_melee", 0, "bonus_icon_melee", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("bonus_icon_accuracy", 0, "bonus_icon_accuracy", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("bonus_icon_speed", 0, "bonus_icon_speed", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("bonus_icon_reload", 0, "bonus_icon_reload", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("bonus_icon_artillery", 0, "bonus_icon_artillery", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("bonus_icon_commander", 0, "bonus_icon_commander", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  
  #Artillery icons
  ("arty_icon_take_ammo", 0, "arty_icon_take_ammo", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("arty_icon_put_ammo", 0, "arty_icon_put_ammo", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("arty_icon_ram", 0, "arty_icon_ram", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("arty_icon_move_up", 0, "arty_icon_move_up", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("arty_icon_take_control", 0, "arty_icon_take_control", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  
  #Medic icons
  ("medic_icon_heal", 0, "medic_icon_heal", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("medic_icon_medic", 0, "medic_icon_medic", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  
  #Stuff
  ("item_select_no_select", 0, "cb_ui_title_panel", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("mm_spyglass_ui", 0, "mm_spyglass_ui_mesh", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("custom_mp_ui_order_button", 0, "mp_ui_order_button", 0, 0, 0, 0, 0, 0, 0.8, 0.6, 0.6),
  
  # Single player stuff
  # Maps
 # ("europe_map_full", 0, "europe_map_full", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  
  # Backgrounds
 # ("memoir", 0, "memoir", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("campmenu", 0, "campmenu", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  
  # Icons
#  ("battle_icon", 0, "battle_icon", 0, 0, 0, 0, 0, 0, 1, 1, 1),
 # ("french_flag_icon", 0, "french_flag_icon", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("compass", 0, "compass", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  
  # On screen indicators
  ("target_plate", 0, "target_plate", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  

  # Admin panel map selection
  ("scn_mp_floodplain_select", 0, "scn_mp_floodplain_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_siege_of_toulon_select", 0, "scn_mp_siege_of_toulon_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_fort_hohenfels_select", 0, "scn_mp_fort_hohenfels_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_fort_george_select", 0, "scn_mp_fort_george_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_fort_mackinaw_select", 0, "scn_mp_fort_mackinaw_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_fort_nylas_select", 0, "scn_mp_fort_nylas_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_charge_of_the_rhine_select", 0, "scn_mp_charge_of_the_rhine_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_fort_de_charte_select", 0, "scn_mp_fort_de_charte_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_fort_brochet_select", 0, "scn_mp_fort_brochet_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_fort_bashir_select", 0, "scn_mp_fort_bashir_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_fort_al_hafya_select", 0, "scn_mp_fort_al_hafya_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_citadell_napoleon_select", 0, "scn_mp_citadell_napoleon_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_venice_select", 0, "scn_mp_venice_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_sjotofta_select", 0, "scn_mp_sjotofta_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_saints_isle_select", 0, "scn_mp_saints_isle_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_russian_town_select", 0, "scn_mp_russian_town_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_outlaws_den_select", 0, "scn_mp_outlaws_den_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_russian_river_select", 0, "scn_mp_russian_river_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_the_island_select", 0, "scn_mp_the_island_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_bavarian_river_select", 0, "scn_mp_bavarian_river_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_forest_pallaside_select", 0, "scn_mp_forest_pallaside_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_countryside_select", 0, "scn_mp_countryside_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_dust_select", 0, "scn_mp_dust_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_beach_select", 0, "scn_mp_beach_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_arabian_town_select", 0, "scn_mp_arabian_town_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_ambush_select", 0, "scn_mp_ambush_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),  
  
  ("scn_mp_arabian_harbour_select", 0, "scn_mp_arabian_harbour_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_arabian_village_select", 0, "scn_mp_arabian_village_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_ardennes_select", 0, "scn_mp_ardennes_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_avignon_select", 0, "scn_mp_avignon_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_bordino_select", 0, "scn_mp_bordino_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_champs_elysees_select", 0, "scn_mp_champs_elysees_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_columbia_farm_select", 0, "scn_mp_columbia_farm_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_european_city_summer_select", 0, "scn_mp_european_city_summer_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_european_city_winter_select", 0, "scn_mp_european_city_winter_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_fort_beaver_select", 0, "scn_mp_fort_beaver_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_fort_boyd_select", 0, "scn_mp_fort_boyd_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_fort_fleetwood_select", 0, "scn_mp_fort_fleetwood_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_fort_lyon_select", 0, "scn_mp_fort_lyon_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_fort_refleax_select", 0, "scn_mp_fort_refleax_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_fort_vincey_select", 0, "scn_mp_fort_vincey_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_french_farm_select", 0, "scn_mp_french_farm_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_german_village_select", 0, "scn_mp_german_village_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_hougoumont_select", 0, "scn_mp_hougoumont_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_hungarian_plains_select", 0, "scn_mp_hungarian_plains_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_la_haye_sainte_select", 0, "scn_mp_la_haye_sainte_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_landshut_select", 0, "scn_mp_landshut_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_minden_select", 0, "scn_mp_minden_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_oaksfield_select", 0, "scn_mp_oaksfield_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_quatre_bras_select", 0, "scn_mp_quatre_bras_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_river_crossing_select", 0, "scn_mp_river_crossing_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_roxburgh_select", 0, "scn_mp_roxburgh_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_russian_village_select", 0, "scn_mp_russian_village_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_schemmerbach_select", 0, "scn_mp_schemmerbach_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_slovenian_village_select", 0, "scn_mp_slovenian_village_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_spanish_farm_select", 0, "scn_mp_spanish_farm_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_spanish_mountain_pass_select", 0, "scn_mp_spanish_mountain_pass_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_spanish_village_select", 0, "scn_mp_spanish_village_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_strangefields_select", 0, "scn_mp_strangefields_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_swamp_select", 0, "scn_mp_swamp_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_walloon_farm_select", 0, "scn_mp_walloon_farm_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_testing_map_select", 0, "scn_mp_testing_map_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_random_plain_select", 0, "scn_mp_random_plain_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_random_steppe_select", 0, "scn_mp_random_steppe_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_random_desert_select", 0, "scn_mp_random_desert_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_random_snow_select", 0, "scn_mp_random_snow_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ##ilam
  ("players_list", 0, "players_list", 0, 0, 0, 0, 0, 0, 1, 1, 1),

  ("score_board_bg", 0, "scoreboard_top", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  
  ("hp_bar_human_icon", 0, "hp_bar_human_icon", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("hp_bar_human_icon_french", 0, "hp_bar_human_icon_french", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("hp_bar_human_icon_prussian", 0, "hp_bar_human_icon_prussian", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("hp_bar_human_icon_russian", 0, "hp_bar_human_icon_russian", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("hp_bar_human_icon_austrian", 0, "hp_bar_human_icon_austrian", 0, 0, 0, 0, 0, 0, 1, 1, 1),
#  ("hp_bar_human_icon_rheinbund", 0, "hp_bar_human_icon_rheinbund", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("hp_bar_horse_icon", 0, "hp_bar_horse_icon", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  
  #new map added in 1.2 but missing the image..
  ("scn_mp_pyramids", 0, "scn_mp_pyramids_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_naval", 0, "scn_mp_naval_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_custom_map", 0, "scn_mp_custom_map_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("scn_mp_wiss", 0, "scn_mp_wiss_select", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  ("white_plane_for_hpbar", 0, "white_plane_new", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  
  ("restore_game_panel_down", 0, "restore_game_panel_down", 0, 0, 0, 0, 0, 0, 1, 1, 1),
  
  
  ("meshes_end", 0, "ui_kingdom_shield_neutral", 0, 0, 0, 0, 0, 0, 1, 1, 1),
]