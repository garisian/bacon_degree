import bacon_functions

if __name__ == '__main__':
    actor_data = open('large_actor_data.txt','r')
    
    # Changes the actor_data and actor_dict into dictionaries that we can use
    actor_dict = bacon_functions.parse_actor_data(actor_data)
    movie_dict = bacon_functions.invert_actor_dict(actor_dict)   
    
    counter = 'continue'
    bacon_number_list = []
    
    while counter == 'continue':
    # As long as counter is 'continue', while loop will continue running
        
        # Take the raw input and remove all unnecessary spaces
        actor_name = raw_input\
                   ('Please enter an actor (or press return to exit): ').strip()
        if actor_name != '':
            
            # If Kevin Bacon is not in the list and he is being searched, print
            # bacon number is infinity and gets rid of roman numerals
            if 'Kevin Bacon' == bacon_functions.fix_actor_name(actor_name) and\
               'Kevin Bacon' not in actor_dict: 
                print 'Kevin Bacon has a Bacon Number of Infinity.' + '\n'
                
            # Exception: if the title of actor_name is 'Kevin Bacon', 
            # return 0 as the Bacon Number. (gets rid of roman numerals)           
            elif bacon_functions.fix_actor_name(actor_name) == 'Kevin Bacon':
                print bacon_functions.fix_actor_name(actor_name) + \
                      ' has a Bacon Number of 0.' + '\n'
            
            # For all other cases....
            else:
                
                # If the raw input is not Kevin Bacon, finds actor_name along 
                # with the bacon_number
                actor_name = bacon_functions.fix_actor_name(actor_name)
                bacon_number = bacon_functions.find_bacon_number(\
                    bacon_functions.find_connection(actor_name,actor_dict,\
                                                   movie_dict),actor_name)
                
                # if the bacon number is infinity, return the following phrase
                if bacon_number == 'Infinity':
                    print bacon_functions.fix_actor_name(actor_name) + \
                          ' has a Bacon Number of ' + bacon_number + '.' + '\n'
                
                # If Bacon number is a finite number, return that folowing 
                # phrase
                else:
                    print bacon_functions.fix_actor_name(actor_name) + \
                          ' has a Bacon Number of ' + bacon_number + '.'
                connection_list = bacon_functions.find_connection(actor_name,\
                                                                 actor_dict,\
                                                                 movie_dict)
                
                
                for actor_movie in connection_list: # for each tuple in the \
                    list
                    if connection_list.index(actor_movie) == 0:
                        
                        # If there is only one tuple in the connection_list,
                        # The actor is directly connected to Kevin Bacon through
                        # one move, hence print the following phrase
                        if len(connection_list) == 1:
                            print bacon_functions.fix_actor_name(actor_name) +\
                                  ' was in ' + actor_movie[0] + ' with ' + \
                                  actor_movie[1] + '.' + '\n'
                        
                        # Otherwise.. Print this tuple's phrase and move on to
                        # the next tuple
                        else:
                            print bacon_functions.fix_actor_name(actor_name) +\
                                  ' was in ' + actor_movie[0] + ' with ' + \
                                  actor_movie[1] + '.'
                            actor = actor_movie[1] 
                    
                    # For all tuples after the first tuple..
                    else:
                        
                        # Works only if the last tuple is reached
                        if (connection_list.index(actor_movie) + 1) == \
                           len(connection_list):
                            print actor + ' was in ' + actor_movie[0] + \
                                  ' with ' + actor_movie[1] + '.' + '\n'

                        # If last tuple hasn't been reached..
                        else:
                            print actor + ' was in ' + actor_movie[0] + \
                                  ' with ' + actor_movie[1] + '.'      # + '\n'
                            actor = actor_movie[1]
                # If bacon number is not infinity, append the number into the
                # bacon_number_list list
                if bacon_number != 'Infinity':
                    bacon_number_list.append(int(bacon_number)) 
        # Break if our next raw input is return
        else:
            counter = 'stop'
            
    # If list is empty, print 0 bacon number
    if bacon_number_list == []:
        print\
             'Thank you for playing! The largest Bacon Number you found was 0.'\
             + '\n'
    
    # Otherwise.. print the highest bacon number found
    else:
        print 'Thank you for playing! The largest Bacon Number you found was '\
              + str(max(bacon_number_list)) + '.' + '\n'