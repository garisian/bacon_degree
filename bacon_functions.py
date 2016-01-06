def item_with_lowest_length(connection):
    '''Return a number which represents the lowest number in connection. 
    Connection must be in the form of a list'''
    
    if len(connection) == 1:            # If only one item in connection,
        final_item = connection[0]      # return that item                                       
        
    elif len(connection) == 0:          # If no items in conncetion, return 
        final_item = []                 # empty list
        
    elif len(connection) > 1:
        length = len(connection[0])
        for item in connection:         # Checks each item in connection and 
            if len(item) < length:      # finds the lowest item            
                final_item = item 
                length = len(final_item) # Changes length so loop goes through
    return final_item                    # each item in the list
    


def fix_actor_name(actor_name):
    '''Return a string with just the actor name from the string actor_name
    The string returned will be capitalized as proper names should have a 
    capital letter at the start'''
    
    if actor_name.count('(') == 1:
        
        # Find the first occurance of '(' from a string such as 'Kevin Bacon 
        # (V)' Cuts everything after first occurance of the open bracket. This
        # can either be a roman numeral in the bracket, and if ther are none, 
        # removes the year
        actor_name = actor_name[0:actor_name.find('(')] 
    
    actor_name_list = actor_name.split() # Removes all unnecessary spaces
                                         # before and after the name
                                                                     
    return actor_name.title()            # Returns the name with the first 
                                          # letter capitalized
        

def invert_actor_dict(actor_dict):
    '''Return a dictionary that is the inverse of actor_dict. The original 
    actor_dict maps actors (string) to lists of movies (string) in which they 
    have appeared. The returned dictionary maps movies (string) to lists of 
    actors (string) appearing in the movie.'''
    
    inversed_actor_dict = {}
    if actor_dict == {}:                        # If the dictionary is empty,
        return {}                               # return an empty dictionary
    else:
        for actor in actor_dict: 
            for movie in actor_dict[actor]:
                
                #Checks every movie for every actor in act_dict.
                if movie not in inversed_actor_dict:  
                    
                    #if the movie is not in the dictionary, add it with the list
                    #of its actors
                    inversed_actor_dict[movie] = list([actor])   
                
                else:
                    
                    #if the movie already exists in the dictionary, simply add 
                    #the actors to that list
                    if actor not in inversed_actor_dict[movie]:
                        inversed_actor_dict[movie].append(actor)    
                    else:
                        pass
        return inversed_actor_dict 

    
def get_actor_name(line):
    '''Return only the actor's firs tand last name from line. line must be in a 
    string format, and actor_name (the returning value) will be in a string 
    form. '''
    
    if line == '':                             # If the string line is empty, 
        actor_name = ''                        # the name is also empty
    elif line != '':
        line_list = line.strip().split('\t')   # remove all unnecessary tabs 
        actor_name = line_list[0]              # and spaces within the string 
        if actor_name.count(',') == 0:        # line
            
            #If there are no commas, call the fix_actor_name, get the name
            #return and strip it
            actor_name = fix_actor_name(actor_name).strip()  
            
        elif actor_name.count(',') == 1:
            
            #If there is a comma, the first name and last name are inverted 
            #Ex: Bacon, Kevin
            sorted_actor_list = actor_name.split(',')    
            
            # The first item after the strip will be the last name
            last_name = sorted_actor_list[0].strip()    
            second_half = sorted_actor_list[1].strip().split()
            
            # This will be the first name after striping the list twice
            first_name = second_half[0]                 
            actor_name = first_name + ' ' + last_name    
    return actor_name


def get_movie_name(line):
    '''Take a string of line and return the movie name and year within the line.
    line bust be in the form of a string. Return movie_list, the movie name, in 
    form of a string.'''
    
    stripped_line = line.strip()  
    
    #Returns the string from index 0 till first sight of ')', which is in the 
    #year. Ex: Kevin Bacon (2009)
    movie_list = stripped_line[0:stripped_line.find(')') + 1] 
    
    return movie_list


def parse_actor_data(actor_data): 
    '''Return the actor information in the open reader actor_data as a 
    dictionary. actor_data contains movie and actor information in IMDB's 
    format. The returned dictionary contains the names of actors (string) as 
    keys and lists of movies (string) the actor has been in as values.'''
    if actor_data == '':
        return []     # If actor_data is empty, return []
    else:        
        actor_dict = {}
        line2 = actor_data.readline()
        while line2.strip().startswith('THE ACTORS LIST') != True:
            #skips the headers and gets to the line that says 'THE ACTORS LIST' 
            line2 = actor_data.readline()
        while line2.strip().startswith('Name') != True:
            #skips the next lines after 'THE ACTORS LINE' has been reached in 
            #order get to the line that states 'NAME'
            line2 = actor_data.readline()
        while line2.strip().startswith('---') != True:
            line2 = actor_data.readline()
            #skips the lines to get to the line that has '----'
        while line2.strip().startswith('') == False:
            #skips the  lines to get to the line that has the data 
            line2 = actor_data.readline() 
        
        for line in actor_data:
            if line[0:4] != '----' and line.startswith('\t') == False and \
               line.strip() != '':
                #If loop gets the lines that have both an actor name and 
                #if there a movie name beside it, and  If line[0:4] != '----' is 
                # so that was an extra line after NAME it wouldn't read it. 
                #line.starts with ('\t') == False is for not having lines that 
                #have just movies in them. line.strip != '' is for having lines 
                # that are not empty.
                actor_name = get_actor_name(line.strip().split('\t')[0])
                #gets the actor_name which will be before the tab and arranging 
                #it using the helper function. 
                rest_of_the_line = ''
                if len(line.strip().split('\t')) > 1: 
                    #just in case line may only have actor name and not a movie 
                    #name 
                    for item in line.strip().split('\t')[1:]:
                        #to get the stuff after the actor name
                        rest_of_the_line += item
                        #adding the stuff to a string 
                    all_movies = [get_movie_name(rest_of_the_line.strip())]
                    #get the movie name from the string 
            if line[0:4] != '----' and line.startswith('\t') == True and \
               line.strip() != '' and line.startswith('\n') == False:
                #this is for lines that only have movie name in it and is 
                # followed 
                #by the line that contains both the actor name and movie name 
                stripped_line = line.strip()
                #stripped the line to get rid of the tabs and get to the content 
                #of the line 
                if get_movie_name(stripped_line) not in all_movies:
                    #just in case two movies the actor was in have the same name
                    all_movies.append(get_movie_name(stripped_line))
                    #add that movie to all_movies 
                    #all_movies has all the movies for that particular actor 
            if line.strip() == '' and line[0:4] != '----':
                #this blank line comes after the data for the particular actor 
                if actor_name in actor_dict:  #If actor exists in the dict
                                               # add the new movie to the others
                    actor_dict[actor_name]=actor_dict[actor_name]+ all_movies
                else:
                    actor_dict[actor_name] = all_movies # make a new key with 
                                                         # actors name and movie
                lst=[]   
                for movie in actor_dict[actor_name]:
                    if movie in lst:            # If movie is a duplicate,
                        pass                    # ignore it
                    else:
                        lst.append(movie)       # add it
                actor_dict[actor_name]= lst
            if line[0:4].strip() == '----':
                #this indicates the end of the data and so break is used to end 
                #to for loop 
                break
        return actor_dict  

def sub_path_returner(coactor, movie, actor_check):
    '''Return a list of the path from actor_check and add coactor to the front 
    the actor_check list and movie right after. Append all item in list to the 
    new list 'new_path' and return the list'''
    
    #add coactor first and movie after in the new path
    new_path = []
    new_path.append(coactor)
    new_path.append(movie)
    
    #add the rest of the items in actor_check in order to new path 
    #and return the list
    for thing in actor_check:
        new_path.append(thing)
    
    return new_path


def final_answer(actor_A, actor_dict, movie_dict):
    '''Return a list of the path from Kevin Bacon to actor_A with the movie
    both actors played in between them. Ex: ['Kevin Bacon','m1','actor_1',
    'm3','actor_A']. List was created with help of the sub_path_returner 
    method'''
    
    done = []  # list of the actors that have been checked
    checking = [[actor_A]]#list of actors with their path that need to be 
                           # checked
    
    if 'Kevin Bacon' not in actor_dict:      # There is a possiblity that Kevin
        return []                            # Bacon isn't in the actor_dict
    
    else:
        if actor_A not in actor_dict:        # There is a possiblity that 
            return []                        # actor_A isn't in the actor_dict
        
        else:
            for actor_checking in checking:
                
                # adds ONLY the actor's name from checking into the done list
                done.append(actor_checking[0])  
                
                # finds all movies acted by actor_checking[0]
                for movie in actor_dict[actor_checking[0]]:    
                    
                    # finds the costar that acted in 'movie'
                    for costar in movie_dict[movie]:           
                        if costar == 'Kevin Bacon':
                            
                            # if costar is Kevin Bacon, return the costar
                            # with his path
                            final_path = sub_path_returner\
                                      (costar,movie,actor_checking) 
                            
                            return final_path                       
                        else:
                            if costar not in done:
                                
                                # if costar isn't Kevin Bacon, take the costar 
                                # and his path and add it to checking list
                                sub_path = sub_path_returner\
                                        (costar,movie,actor_checking) 
                                checking.append(sub_path)
            
            return []            # Only reaches this line if Kevin Bacon isn't 
                                 # found. Therefore returns an empty list, as 
                                 # the Bacon number is Infinity

        
def find_connection(actor_A, actor_dict, movie_dict):
    '''Return a list of (movie, actor) tuples (both elements of type string)
    that represent a shortest connection between actor_name and Kevin Bacon that
    can be found in the actor_dict and movie_dict. (These dictionaries were 
    produced by parse_actor_data and invert_actor_dict, respectively.) Each 
    tuple in the returned list has a special property: the actor from the
    previous tuple and the actor from the current tuple both appeared in the 
    stated movie. For the first tuple, the "actor from the previous tuple" is 
    actor_name, and the last tuple must contain Kevin Bacon. If there is no 
    connection between actor_name and Kevin Bacon, the returned list is 
    empty.'''
    
    # Convert the list from the form 
    # (Kevin_Bacon, movie_1,Actor_2,.......,actor_A) into the proper from of 
    # [(....,.....)(....,Actor_2),(movie_1,Kevin_Bacon)]
    actor_A = actor_A.title()
    if 'Kevin Bacon' == actor_A:
        return []
    else:
        actor_title = actor_A
        tester = final_answer(actor_title, actor_dict, movie_dict)    
        lst = []
        
        p = len(tester) - 2   # Since actor_A shouldn't be in the final result,  
                            # start at the index right before actor_A, which is 
                            # len(d)-2
        while p > 0:
            lst.append((tester[p],tester[p - 1]))# Starting from index p, make 
                                       # a tuple of every 2 elements in the list 
                                       # and add it to list lst
            p -= 2                       # Since the previous line deals with 
                                       # the last wo elements, we need to change 
                                       # p to the index value of the next item,  
                                       # which is 2 less than p
        return lst                                        
                   

def find_bacon_number(connection, actor_name):
    '''Return a number which is the bacon number of the connection. Argument for
    metod must be in the form of a list. actor_name is the raw input by the user
    '''
    
    if fix_actor_name(actor_name) == 'Kevin Bacon': # If the input (actor_name)
        bacon_number = '0'                          # is 'Kevin Bacon', return 0 
        
    else:
        if connection == []:                      # If the connection list is  
            bacon_number = 'Infinity'             # empty, bacon_number in empty
        
        else:
            bacon_number = str(len(connection))   # Each item in connection is 
                                                  # the bacon number. Find the 
                                                  # length and return the value
    return bacon_number 