import printing_models_module as pmm

unprinted_designs = ["iPhoneケース", "ロボットのペンダント", "12面体"]
completed_models = []

pmm.print_models(unprinted_designs, completed_models)
pmm.show_completed_models(completed_models)