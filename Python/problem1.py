def shortcut( s ):
    bad_char = ['a', 'e', 'i', 'o', 'u']
    for x in s.lower():
        if x in bad_char:
            s = s.replace(x, '')
    return(s)