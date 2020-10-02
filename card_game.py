#!/usr/bin/env python
# coding: utf-8

# In[43]:


#CARD GAME(WAR)
import random
suits=('spades','diamonds','hearts','clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,
          'Jack':11,'Queen':12,'King':13,'Ace':14}


# In[44]:


class Card:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
        
    def __str__(self):
        return self.rank + ' of ' +self.suit


# In[45]:


three_of_clubs=Card('clubs','Three')


# In[46]:


print(three_of_clubs)


# In[47]:


two_hearts=Card('hearts','Two')


# In[48]:


two_hearts


# In[49]:


two_hearts.suit


# In[50]:


two_hearts.rank


# In[51]:


print(two_hearts)


# In[52]:


#values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,
         # 'Jack':11,'Queen':12,'King':13,'Ace':14}


# In[53]:


two_hearts.value<=three_of_clubs.value


# In[54]:


two_hearts.value==three_of_clubs.value


# In[55]:


class Deck:
    
    def __init__(self):
        
        self.all_cards=[]
        
        for suit in suits:
            for rank in ranks:
                created_card=Card(suit,rank)
                
                self.all_cards.append(created_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)#for shuffling....1.from random import shuffle
                                                    #2.random.shuffle(mylist)
            
    def deal_one(self):
        return self.all_cards.pop()


# In[56]:


new_deck = Deck()


# In[57]:


first_card=new_deck.all_cards[0]


# In[58]:


print(first_card)


# In[59]:


bottom_card=new_deck.all_cards[-1]


# In[60]:


print(bottom_card)


# In[61]:


for card_object in new_deck.all_cards:
    print(card_object)


# In[62]:


new_deck.shuffle()


# In[63]:


print(new_deck.all_cards[-1])


# In[64]:


mycard=new_deck.deal_one()


# In[65]:


print(mycard)


# In[66]:


len(new_deck.all_cards)


# In[67]:


class Player:
    
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
        #list of multiple card obj
            return self.all_cards.extend(new_cards)
        else:
            #for single card obj
            return self.all_cards.append(new_cards)
    
           
    def __str__(self):
        return f'Player {self.name}  has {len(self.all_cards)} cards'


# In[68]:


new_player= Player('Afrin')


# In[69]:


print(new_player)


# In[70]:


new_player.add_cards(mycard)


# In[71]:


new_player


# In[72]:


print(mycard)


# In[73]:


print(new_player)


# In[74]:


print(new_player.all_cards[0])


# In[75]:


new_player.add_cards([mycard,mycard,mycard])


# In[76]:


print(new_player)


# In[77]:


new_player.remove_one()


# In[78]:


print(new_player)


# In[79]:


# Game play


# In[80]:


player_one=Player('One')
player_two=Player('Two')

new_deck=Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
    


# In[81]:


print(player_one.all_cards[0])


# In[82]:


game_on=True


# In[83]:


round_no=0

while game_on:
    
    round_no+=1
    print(f'round {round_no}')
    
    if len(player_one.all_cards)==0:
        print('player 1 out of cards,player 2 wins!')
        game_on= False
        break
        
        
    if len(player_two.all_cards)==0:
        print('player 2 out of cards,player 1 wins!')
        game_on= False
        break
        
        
    #start a new round
    
    player_one_card=[]
    player_one_card.append(player_one.remove_one())
    
    player_two_card=[]
    player_two_card.append(player_two.remove_one())
    
    
    
    at_war = True

    while at_war:
        if player_one_card[-1].value> player_two_card[-1].value:
            player_one.add_cards(player_one_card)
            player_one.add_cards(player_two_card)
        
            at_war= False
        
        elif player_one_card[-1].value< player_one_card[-1].value:
            player_two.add_cards(player_one_card)
            player_two.add_cards(player_two_card)
        
            at_war=False
        
        else:
            print('WAR')
        
            if len(player_one.all_cards)<5:
                print('Player 1 unable to declare war')
                print('Player 2 wins!')
                game_on = False
                break
        
            elif len(player_two.all_cards)<5:
                print('Player 2 unable to declare war')
                print('Player 1 wins!')
                game_on = False
                break
        
            else:
                for num in range(5):
                    player_one_card.append(player_one.remove_one())
                    player_two_card.append(player_two.remove_one())
            
        
        
        
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




