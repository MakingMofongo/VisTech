    global OBJECTS
    global BOT
    BOT = bot_initialize()
    print('BOT INITIALIZED')
    ELTTS.speech('bot INITIALIZED')
    test_string = 'Text: Shop, Objects: car'
    print('Testing BOT with string: ',test_string)
    ELTTS.speech('Testing bot with string: '+test_string)
    response = description(BOT,test_string)
    print(f"Response: {response}")
    ELTTS.speech('Response: '+str(response[1]))
    main(cap,initial_index)