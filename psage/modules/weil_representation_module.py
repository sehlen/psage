r"""

Classes for Weil representations associated with
 - Finite quadratic modules (eq. with even lattices)
 - Lattices (both odd and even)

"""

from sage.modules.free_module import FreeModule_generic_pid,FreeModule_ambient_pid,FreeModule_submodule_with_basis_pid,FreeModule_generic
from sage.all import ZZ
from sage.structure.element import ModuleElement
from sage.misc.cachefunc import cached_method

class WeilModule_generic(FreeModule_generic):
    r"""
    Generic Weil representation module. This is a free ZZ-module with an SL_{2}(ZZ) or MP_{2}(ZZ) action.
    """
    def __init__(self,base_ring,rank,degree):
        r"""
        Initialize a Weil representation module of rank n over the ring R.
        """
        super(WeilModule_generic,self).__init__(base_ring,rank,degree)

    def __repr__(self):
        r"""
        Representing self.
        """
        return "Generic Weil module of rank {0} and degree {1}".format(self.rank(),self.degree())

        
    ## The methods we want to have
    def lattice(self):
        r"""
        Return the lattice associated with self (if it exists)
        """
        raise NotImplementedError("Should be overriden by subclasses")

    def finite_quadratic_module(self):
        r"""
        Return the finite quadratic module associated with self (if it exists)
        """
        raise NotImplementedError("Should be overriden by subclasses")

    def invariants(self):
        r"""
        Return the space of invariants of self under the SL(2,Z) action.
        """
        raise NotImplementedError

    def sl2_action_on_basis(self,A):
        r"""
        Return the matrix given by the action of an element in SL(2,O) on self.basis()
        """
        raise NotImplementedError
    
        
class WeilModule_ambient_pid(WeilModule_generic,FreeModule_ambient_pid):
    r"""
    Weil representation module. This is a free ZZ-module with an SL_{2}(ZZ) or MP_{2}(ZZ) action.
    """
    def __init__(self,base_ring,rank,degree):
        r"""
        Initialize a Weil representation module of rank n over the ring R.
        """
        super(WeilModule_ambient_pid,self).__init__(base_ring,rank,degree)



    def __repr__(self):
        r"""
        Representing self.
        """
        return "Ambient Weil module of rank {0} and degree {1}".format(self.rank(),self.degree())
    
    
class WeilModule_submodule_with_basis_pid(WeilModule_generic,FreeModule_submodule_with_basis_pid):
    r"""
    A submodule of a Weil module.
    """
    def __init__(self,ambient,basis,gens):
        r"""
        Initialize a generic submodule of a Weil module.
        """
        assert isinstance(Sequence(gens).universe(),WeilModule_generic)
        self._ambient_module = ambient
        rank = len(basis)
        super(Weilmodule_submodule_with_basis_pid,self).__init__(ambient.base_ring(),rank,ambient.degree())

        
    def ambient_module(self):
        r"""
        Return the ambient module of self.
        """
        return self._ambient_module

class WeilModule_invariant_submodule(WeilModule_submodule_with_basis_pid):
    r"""
    A submodule of SL2(Z) invariants of a Weil module
    """
    def __init__(self):
        r"""
        Initialize a submodule of SL2(Z) invariants of a Weil module
        """
        pass

        
class WeilModule_element_generic(ModuleElement):
    r"""
    Elements of a Weil module
    """

    def __init__(self,parent,coords,name=None,function=None):        
        r"""
        Initialize an element of a Weil module.
        """
        self._coords = coords
        self._name
        super(WeilModule_element_generic,self).__init__(parent)

    def __repr__(self):
        r"""
        Represent self.
        """
        if self._name<>None:
            return self._name
        return "An element of a generic Weil module. Coords:={0}".format(self.coords())

    def coords(self):
        r"""
        Return the coordinates of self in terms of the basis of self.parent()
        """
        return self._coords
    
    @cached_method 
    def __call__(self,x):
        r"""
        Act by self on `x` in `L^{\bullet}`
        """
        assert x in self.parent().lattice().bullet_elements()
        return self._function(x)
        
    def action_of_sl2z(self,A):
        r"""
        
        """
        raise NotImplementedError
    
def WeilModule_invariant_class(WeilModuleElement_generic):
    r"""
    Invarants of a Weil module. 
    """

    def __init__(self,parent,function=None):        
        r"""
        Initialize an invariant element of a Weil module.
        """
        pass


    def action_of_sl2z(self,A):
        r"""
        Since self is invariant this always return the
        identity map.
        """
        return 1


class WeilRepresentationOfLAttice(WeilModule_generic):
    r"""
    Implements the set W(L) for a lattice L.
    Here W(L) consitst of lambda:L^{bullet) ---> CC
    s.t. lambda(r+x)=e(beta(x))*lambda(r), for all r in L^bullet
    and x in L.


    """
    def __init__(self):
        pass
