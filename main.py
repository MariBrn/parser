from lib import pre_parser, parser, post_parser

if __name__ == "__main__":

    keywords = ("DATES", "COMPDAT", "COMPDATL")
    parameters = ("Date", "Well name", "Local grid name", "I", "J", "K upper", "K lower", "Flag on connection",
                  "Saturation table", "Transmissibility factor", "Well bore diameter", "Effective Kh",
                  "Skin factor", "Skin factor", "Skin factor", "D-factor")

    input_file = "input_data/test_schedule.inc"
    clean_file = "output_data/handled_schedule.inc"
    output_csv = "output_data/schedule.csv"

    cleaned_schedule = pre_parser.clean_schedule(input_file=input_file, output_file=clean_file)

    schedule_list = parser.parse_schedule(cleaned_schedule=cleaned_schedule, keywords=keywords)

    post_parser.transform_schedule(schedule_list=schedule_list, parameters=parameters, output_csv=output_csv)
