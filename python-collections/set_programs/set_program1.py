#define empty set:define set()
#insertion order is not preserved

#update is possible
#duplicate are not allowed
#empty {}(brackets), taken as dictionary if u want to create an empty set use set()

#st=set()
#print(type(st))

st={2,4,6,8,"hai","hello",8,9,10}
st2={12,13}
st.update(st2)
print(st)

