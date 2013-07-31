r"""
Implements basic classes for modules over rings with an additional
 action by a group.


 AUTHOR: Fredrik Stromberg
 
"""

#*****************************************************************************
#       Copyright (C) 2013 Fredrik Stromberg <fredrik314@gmail.com>
#
#  Distributed under the terms of the GNU General Public License (GPL)
#                  http://www.gnu.org/licenses/
#*****************************************************************************


from sage.modules.free_module import FreeModule_generic_pid,FreeModule_ambient_pid,FreeModule_submodule_with_basis_pid,FreeModule_generic,FreeModule_ambient,FreeModule_submodule_pid
from sage.all import ZZ,Sequence
from sage.structure.element import ModuleElement
from sage.misc.cachefunc import cached_method
from sage.rings.principal_ideal_domain import is_PrincipalIdealDomain

class ModuleWithGroupAction_generic(FreeModule_generic):
    r"""
    Generic Weil representation module. This is a free ZZ-module with an SL_{2}(ZZ) or MP_{2}(ZZ) action.
    """
    def __init__(self,base_ring,rank,degree,group):
        r"""
        Initialize a Weil representation module of rank n over the ring R.
        EXAMPLES::

            sage: from sage.all import SL2Z
            sage: M=ModuleWithGroupAction_generic(ZZ,3,3,SL2Z); M
            Generic Module of rank 3 and degree 3 with action by Modular Group SL(2,Z)
            
        """
        self._group = group
        self._element_class = ModuleWithGroupAction_generic_element
        #       super(ModuleWithGroupAction_generic,self).__init__(base_ring,rank,degree,sparse=False)
        FreeModule_generic.__init__(self,base_ring,rank,degree)
        
    def __repr__(self):
        r"""
        Representing self.

        EXAMPLES::

        
            sage: from sage.all import SL2Z
            sage: M=ModuleWithGroupAction_generic(ZZ,3,3,SL2Z); M
            Generic Module of rank 3 and degree 3 with action by Modular Group SL(2,Z)
        """
        return "Generic Module of rank {0} and degree {1} with action by {2}".format(self.rank(),self.degree(),self.group())

    def group(self):
        r"""
        Return the group which is acting on self

        EXAMPLES::

        
            sage: from sage.all import SL2Z
            sage: M=ModuleWithGroupAction_generic(ZZ,3,3,SL2Z)
            sage: M.group()
            Modular Group SL(2,Z)

        """
        return self._group

    def invariants(self):
        r"""
        Return the space of invariants of self under the SL(2,Z) action.
        EXAMPLES::

        
            sage: from sage.all import SL2Z
            sage: M=ModuleWithGroupAction_generic(ZZ,3,3,SL2Z)
            sage: M.invariants()
            Traceback (most recent call last)
            ...
            NotImplementedError:
        
        """
        raise NotImplementedError

    def group_action_on_basis(self,g):
        r"""
        Return the matrix given by the action of an element g in self.group()
        EXAMPLES::

        
            sage: from sage.all import SL2Z
            sage: M=ModuleWithGroupAction_generic(ZZ,3,3,SL2Z)
            sage: M.group_action_on_basis(SL2Z.gens()[0])
            Traceback (most recent call last)
            ...
            NotImplementedError:

        """
        raise NotImplementedError
    

class ModuleWithGroupAction_ambient(ModuleWithGroupAction_generic,FreeModule_ambient):
    r"""
    Ambient module with group action.
    """
    def __init__(self,base_ring,rank,degree,group):
        r"""
        Initialize an ambient module with group action.

        EXAMPLES::

        
            sage: from sage.all import SL2Z
            sage: M=ModuleWithGroupAction_ambient(ZZ,3,3,SL2Z)
            sage: M.is_ambient()
            True
        """
        super(ModuleWithGroupAction_ambient,self).__init__(base_ring,rank,degree,group)

    def __repr__(self):
        r"""
        Representing self.

        EXAMPLES::

        
            sage: from sage.all import SL2Z
            sage: M=ModuleWithGroupAction_ambient(ZZ,3,3,SL2Z);M
            Ambient module of rank 3 and degree 3 with action by Modular Group SL(2,Z)

        """
        return "Ambient module of rank {0} and degree {1} with action by {2}".format(self.rank(),self.degree(),self.group())
    
    

class ModuleWithGroupAction_ambient_pid(ModuleWithGroupAction_ambient,FreeModule_ambient_pid):
    r"""
    Ambient module over a PID with group action.
    """
    def __init__(self,base_ring,rank,degree,group):
        r"""
        Initialize an ambient module with group action.

        EXAMPLES::

        
            sage: from sage.all import SL2Z
            sage: M=ModuleWithGroupAction_ambient(ZZ,3,3,SL2Z)
            sage: M.is_ambient()
            True
        """
        assert is_PrincipalIdealDomain(base_ring)
        super(ModuleWithGroupAction_ambient_pid,self).__init__(base_ring,rank,degree,group)

    def __repr__(self):
        r"""
        Representing self.

        EXAMPLES::

        
            sage: from sage.all import SL2Z
            sage: M=ModuleWithGroupAction_ambient(ZZ,3,3,SL2Z);M
            Ambient module of rank 3 and degree 3 with action by Modular Group SL(2,Z)

        """
        return "Ambient module of rank {0} and degree {1} with action by {2}".format(self.rank(),self.degree(),self.group())
    
    


class ModuleWithGroupAction_submodule_pid(ModuleWithGroupAction_generic,FreeModule_submodule_pid):
    r"""
    A submodule of a Weil module.
    """
    def __init__(self,ambient,gens):
        r"""
        Initialize a generic submodule of a Weil module.

        EXAMPLES::

        
            sage: from sage.all import SL2Z
            sage: M=ModuleWithGroupAction_ambient_pid(ZZ,3,3,SL2Z)
            sage: S=ModuleWithGroupAction_submodule_pid(M,M.gens()[0]);S
            Submodule of Ambient module of rank 3 and degree 3 with action by Modular Group SL(2,Z)
        
        
        """
        if not isinstance(gens,(list,tuple)):
            gens = [gens]
        if not isinstance(Sequence(gens).universe(),type(ambient)) or not isinstance(ambient,ModuleWithGroupAction_ambient_pid):
            raise ValueError("Need gens to consist of elements of ambient!")
        self._ambient_module = ambient
        rank = len(gens)
        FreeModule_submodule_pid.__init__(self,ambient,gens)
        ModuleWithGroupAction_generic.__init__(self,ambient.base_ring(),rank,ambient.degree(),ambient.group())
#        super(ModuleWithGroupAction_submodule_pid,self).__init__(ambient.base_ring(),rank,ambient.degree(),ambient.group())

    def __repr__(self):
        r"""
        Represent self.

        EXAMPLES::

        
            sage: from sage.all import SL2Z
            sage: M=ModuleWithGroupAction_ambient_pid(ZZ,3,3,SL2Z)
            sage: S=ModuleWithGroupAction_submodule_pid(M,M.gens()[0]);S
            Submodule of Ambient module of rank 3 and degree 3 with action by Modular Group SL(2,Z)
            
        """
        return "Submodule of {0}".format(self.ambient_module())
        
    def ambient_module(self):
        r"""
        Return the ambient module of self.

        EXAMPLES::

        
            sage: from sage.all import SL2Z
            sage: M=ModuleWithGroupAction_ambient_pid(ZZ,3,3,SL2Z)
            sage: S=ModuleWithGroupAction_submodule_pid(M,M.gens()[0]);S
            Ambient module of rank 3 and degree 3 with action by Modular Group SL(2,Z)

        """
        return self._ambient_module

class ModuleWithGroupAction_invariant_submodule_pid(ModuleWithGroupAction_submodule_pid):
    r"""
    A submodule of SL2(Z) invariants of a Weil module
    """
    def __init__(self,ambient,gens):
        r"""
        Initialize a submodule of SL2(Z) invariants of a Weil module

        EXAMPLES::


        
        """
        super(ModuleWithGroupAction_invariant_submodule_pid,self).__init__(ambient,gens)

        
class ModuleWithGroupAction_generic_element(ModuleElement):
    r"""
    Elements of a module with group action.
    """

    def __init__(self,parent,coords,name=None,function=None):        
        r"""
        Initialize an element of a Weil module.
        """
        self._coords = coords
        self._name = name
        super(ModuleWithGroupAction_generic_element,self).__init__(parent)

    def __repr__(self):
        r"""
        Represent self.
        """
        if self._name<>None:
            return self._name
        return "An element of a generic Weil module. Coords:={0}".format(self.coords())


    def __item__(self,i):
        r"""
        
        """
    
    def coords(self):
        r"""
        Return the coordinates of self in terms of the basis of self.parent()
        """
        return self._coords
    
    def __call__(self,x):
        r"""
        Act by self on `x`
        """
        raise NotImplementedError("Needs to be overriden by subclasses")
        
    def group_action(self,g):
        r"""
        
        """
        raise NotImplementedError

    def __mul__(self,g):
        r"""
        Multiply self by g
        """
        if isinstance(g,self.base_ring):
            return g*self
        elif g in self.group():
            return self.group_action(g)

        
