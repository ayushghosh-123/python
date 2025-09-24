seat_type = input("Enter seat type (sleaper/Ac?general?luxury): ").lower()

match seat_type : 
    case "sleeper":
        print("Sleeper - No Ac, beds available")
    case "ac":
        print('Ac - AIr conditioned , comfy ride')
    case 'gneneral':
        print('"General - Cheapest option, no reservation')
    case 'luxury':
        print('Luxury - Premium seats with meals')
    case _:
        print("Invalid seat type")