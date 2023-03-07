def solution(a):
    '''
        # add matching adjacent neighbors
        ("a",0,0) : [("a",0,1)]
        ("a",0,1) : [("a",0,0)]
        ("b",0,2) : [("b",1,2)]
        ("c",0,3) : [("c",0,4)]
        ("c",0,4) : [("c",0,3), ("c",1,4)]
    '''
    def get_matching_neightbors():
        kmap = dict()
        for idx, row in enumerate(a):
            for col in range(len(row)):
                letter = a[idx][col]
                kmap[(letter,idx,col)] = []
                if idx > 0 and letter == a[idx-1][col]:
                    # look up
                    kmap[(letter,idx,col)].append( (letter, idx-1, col) )
                if idx+1 < len(a) and letter == a[idx+1][col]:
                    # look down
                    kmap[(letter,idx,col)].append( (letter, idx+1, col) )
                if col > 0 and letter == a[idx][col-1]:
                    # look left
                    kmap[(letter,idx,col)].append( (letter, idx, col-1) )
                if col+1 < len(row) and letter == a[idx][col+1]:
                    # look right
                    kmap[(letter,idx,col)].append( (letter, idx, col+1) )
        return kmap

    def get_longest_adjacency_stream(kmap):
        rv = set()
        for k, v in kmap.items():
            # prime our data sets
            stream = set()
            stack  = [k]
            while stack:
                # we will add any adjacent nodes that we haven't seen yet
                # and continue to add their neighbors until we have no
                # more unique neighbors
                vv          = stack.pop()
                sv          = set(kmap[vv])
                new_nodes   = sv - stream
                stack.extend(new_nodes)
                stream.update(new_nodes)
            if len(stream) > len(rv):
                # if we've found a larger cluster, update our return value
                rv = stream
        return next(iter(rv))[0][0], len(rv)

    kmap = get_matching_neightbors()
    return get_longest_adjacency_stream(kmap)

    

if __name__ == "__main__":
    # sample input - assumes rows have identical length
    a = [
        ["a","a","b","c","c"],
        ["b","b","b","a","c"],
        ["a","b","c","c","c"],
    ]
    # expected output: ('c', 6)
    print(solution(a))
