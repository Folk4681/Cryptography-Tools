from collections import OrderedDict
import hashlib,json

class MerkTree:


	def __init__(self,lst=None):
		self.lst = lst
		self.pastLst = OrderedDict()
 
	def create_tree(self):

		lst = self.lst
		pastLst = self.pastLst
		temp_transaction = []


		for index in range(0,len(lst),2):
			now = lst[index]
			if index+1 != len(lst):
				now_right = lst[index+1]
			else:
				now_right = ''

			now_hash = hashlib.sha256(now)

			if now_right != '':
				now_right_hash = hashlib.sha256(now_right)

			pastLst[lst[index]] = now_hash.hexdigest()

			if now_right != '':
				pastLst[lst[index+1]] = now_right_hash.hexdigest()

			if now_right != '':
				temp_transaction.append(now_hash.hexdigest() + now_right_hash.hexdigest())


			else:
				temp_transaction.append(now_hash.hexdigest())

		if len(lst) != 1:
			self.lst = temp_transaction
			self.pastLst = pastLst

			self.create_tree()


	def Get_past_transacion(self):
		return self.pastLst

	def Get_Root_leaf(self):
		last_key = self.pastLst.keys()[-1]
		return self.pastLst[last_key]

if __name__ == "__main__":

	merktree1 = MerkTree()

	"""transaction1 = ['8eab24de5a17ba8b024d89e41d059a5ee292462604424294258b833b3db9b3c2',
			'80b4122731e53f999a63b79bc9172d33c5cc49dfa45d791ea6ec7e0f936622c5',
			'6fd7ff153c7fb6fdaa8c4b0dfb97af358a25b70786934dfe60051b3478c90913',
			'284fc3bff0d49f82c9b8f51f377c42778d784b605e4aef7fe75928965b487058',
			'7a73e3ed513e15f9ac0f7d2bf6b5c079f3ba14036ead60a5603bc7bb4863c58b',
			'9cf185103e91c024db1024f6d73f1bc2e2f111b2453452b4ae4d42a5f3390b0d',
			'f6a85d8a7711e5e1ba99fabdba8f580d8dddf96e985d95f73823e9799ba43663',
			'5af7d87eb6f48a6688240ebdbae542b704253dab1602f5f57108ab4c3fee83b9']
	"""
	transaction1 = ["de9b91239702ca141956c0e5cefcc889bedcd847a3ddfd6e8390a8ef0b4cc7a7", 				"8f6f45bd45f183c58d4fed193d7dc7704604e560dc9638093eca449a60a035d8",
			"434a4800056881b282077f969726fee6a5902d0198a69f04d687188bfd624f03", 				"3d10114441b8211ae2ca81607f1530808b2467e5970ceba1cd735406c67ab5ab",
			"40cbf0c4bcc83ac3465b4635e21dbe5df36ff5a41dec502a6972b8d7ec708569", 				"0253ec06ec8869f14aba11d1ef57bec995dd142f2256cf7eec511799b37d6911",
			"93b797f6d735beb2b636220e5c547a6e8369abd55ecd8b2525ae70d69345e8db", 				"2a25acdaad22a3e78c41a33da6357a3551d1bb4bf43808e5cc37dd8fd9d1c422"]

	merktree1.lst = transaction1
	merktree1.create_tree()
	pastLst = merktree1.Get_past_transacion()
	print 'Final root of the tree : ',merktree1.Get_Root_leaf()


