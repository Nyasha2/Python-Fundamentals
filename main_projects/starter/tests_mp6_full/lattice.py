"""
CS 1 22fa
MP6: Crystal Lattices
Student Name: Nyasha

TODO: 2-3 sentence program overview.
"""
import math
from atom import Atom


# TODO: Implement this CubicLattice class as described in the spec.
# TODO: Include any docstrings that are omitted in methods
# TODO: Remove all TODOs/pass statements when you finish.
class CubicLattice():
    """
    Simple class representation of a cubic lattice. Contains information on the
    represented cubic lattice and the lattice parameters for the crystal.

    Attributes:
        - lparam (int or float): the lattice parameters for the crystal
        - atoms (list):
    """

    def __init__(self, lparam, atoms=[], in_filename=None):
        """
        Construct a CubicLattice instance representing a cubic lattice with lparam
        lattice parameters.

        Arguments:
            - lparam (int or float): the integer or float value of the lattice parameters
            - atoms=[] (a list): This is an optional argument which is a list of atoms with the specified lattice.
            - in_filename=None (file): This is a file that contains information about certain atoms.

        Raises:
            - ValueError if parameter is less than 0
            - FileNotFound error if the file name is invalid.
        """
        if lparam <= 0:
            raise ValueError('lparam must be positive.')

        if in_filename is None:
            self.atoms = atoms
        else:
            self.atoms = self.get_atoms_from_xyz(in_filename)

        self.lparam = lparam

    def get_lattice_parameter(self):
        """
        Returns the latice parameter of the crystal lattice.
        """
        return self.lparam

    def get_cell_volume(self):
        """
        Returns the volume of the cubic lattice.
        """
        return math.pow(self.lparam, 3)

    def get_unique_elements(self):
        """
        Returns a list of all the unique elements contained in the lattice.
        """
        unique_elements = []
        for atom in self.atoms:
            if atom.element not in unique_elements:
                unique_elements.append(atom.element)
        return unique_elements

    def get_number_atoms(self):
        """
        Returns the number of atoms in a given crystal lattice.

        Returns:
            - number_of_toms (float): the number of atoms in the lattice.
        """
        number_of_atoms = 0
        for atom in self.atoms:
            if is_corner(atom.get_coordinates(), self.lparam):
                number_of_atoms += 1 / 8
            elif is_cell_center(atom.get_coordinates(), self.lparam):
                number_of_atoms += 1
            elif is_face_center(atom.get_coordinates(), self.lparam):
                number_of_atoms += 1 / 2

        return number_of_atoms

    def get_inverted_cell(self):
        """
        Returns a new CubicLattice where all the tomms are flipped around the center of the cube.
        """
        inverted_atoms = []
        for atom in self.atoms:
            name = atom.element
            inverted = []
            coordinates = atom.coordinates
            for point in coordinates:
                point = abs(point - self.lparam)
                # if point == 0:
                #     point = self.lparam
                # else:
                #     point = 0
                inverted.append(point)
            inverted_atoms.append(Atom(name, tuple(inverted)))
        return CubicLattice(self.lparam, inverted_atoms)

    def as_xyz(self, crystal_name):
        """
        Returns a string representation of the crystal given
        a specified `crystal_name` that is in standard .xyz file format.

        An XYZ file format is strictly as follows (guaranteeing each
        Atom_I_Element line to be comprised of 4 components):

        # of atoms N
        Name of the crystal (basically a comment)
        Atom_1_Element Atom_1_X Atom_1_Y Atom_1_Z
        Atom_2_Element Atom_2_X Atom_2_X Atom_2_Z
        ...
        Atom_N_Element Atom_N_X Atom_N_Y Atom_N_Z

        For example (16 lines total):
        14
        Aluminum FCC
        Al 0 0 0
        ...
        Al 2.0 2.0 4

        Arguments:
            - crystal_name (str): Name of crystal to specify (the second
              line in .xyz format)

        Returns:
            - (str) .xyz data format of crystal, with each line ending with
              '\n' (including the last)
        """
        string = ''
        string = string + f'{len(crystal_name.atoms)}\n'
        string = string + crystal_name + '\n'
        for atom in crystal_name.atoms:
            string = string + f'{str(atom)}\n'
        return string

    def write_to_xyz(self, crystal_name, out_filename):
        """
        Writes the current crystal to an XYZ file, which is a standard
        file format compatible with 3D crystal-viewing software.
        See `CubicLattice.as_xyz` for more information on the XYZ
        representation.

        Note: Overwrites file if one already exists.

        Arguments:
            - crystal_name (str): Crystal name; the second line in .xyz file.
            - out_filename (str): Filename to write to (should end in .xyz)

        Returns:
            - None (crystal data is written to `out_filename`)
        """
        with open(out_filename, 'w') as file:
            # check if the line below is correct
            crystal_as_xyz = self.as_xyz(crystal_name)
            file.write(crystal_as_xyz)

    def get_atoms_from_xyz(self, in_filename):
        """
        Given an in_filename, returns a list of Atoms created from the file
        specifications, which should be in valid .xyz format.
        See `CubicLattice.as_xyz` for a summary of a valid XYZ format.

        Note that the (x, y, z) coordinates specified by each XYZ Atom line
        are converted to floats for the list of constructed Atoms.

        Arguments:
            - in_filename (str): Name of .xyz file to import (e.g. 'ex1.xyz')

        Returns:
            - (list[Atom]): list of Atoms constructed from imported file data

        Raises:
            - FileNotFoundError if `in_filename` doesn't exist
        """
        # C.3. (reminder, you aren't raising any FileNotFoundError,
        # this is just noted to a client so they know we don't handle this
        # specially)
        atom_info = []
        with open(in_filename, 'r') as file:
            for line in file:
                if file[line] > 1:
                    # we are adding the total information of individual atoms
                    # as an element of a list.
                    atom_info.append(line)

            atoms_list = []
            for atom in atom_info:
                # we are spliting the info of a single atom and putting it into a list
                # something like ['Na', '0.5', '1.0', '0.5]
                element_info = list(atom.split(' '))
                name = element_info[0]
                coordinates = (
                    element_info[1],
                    element_info[2],
                    element_info[3])
                coordinates = (float(i) for i in coordinates)
                element = (name, coordinates)
                atoms_list.append(element)

            return atoms_list


# ----------------------------------------
# END CubicLattice class definition
# ----------------------------------------
# 3 helper _functions_ for lattice coordinates; note that these
# generalize for any 3D cube representation, not just 3D crystal lattices.
# DO NOT CHANGE these three functions.
def is_corner(coordinates, length):
    """
    Returns whether the given coordinates are on a corner of a cube with
    side length `length`.

    Arguments:
        - coordinates (tup/list): (x, y, z) coordinates to test
        - length (int/float): side length of cube

    Returns:
        - (bool): True iff passed coordinates match corners of `length`^3 cube

    Raises:
        - ValueError if the passed coordinates does not have exactly 3 values.
    """
    if len(coordinates) != 3:
        raise ValueError('coordinates must be a 3-element tuple.')

    for coord in coordinates:
        # By definition, each x, y, z value in a coordinate must be 0 or
        # the length of the cube
        if coord != 0 and coord != length:
            return False
    return True


def is_cell_center(coordinates, length):
    """
    Returns whether the given coordinates are at the center of a
    cube with side length `length`.

    Arguments:
        - coordinates (tup/list): (x, y, z) coordinates to test
        - length (int/float): side length of cube

    Returns:
        - (bool): True iff coordinates are the center of `length`^3 cube

    Raises:
        - ValueError if the passed coordinates does not have exactly 3 values.
    """
    if len(coordinates) != 3:
        raise ValueError('coordinates must be a 3-element tuple.')

    for coord in coordinates:
        # By definition, each x, y, z value in a coordinate must be length/2
        # if it is the cube's center
        if coord != length / 2:
            return False
    return True


def is_face_center(coordinates, length):
    """
    Returns whether the given coordinates are on the center of a cube's _face_
    with side length `length`. In other words, they are not at one of the 8
    corners or the center of the cube.

    Arguments:
        - coordinates (tup/list): (x, y, z) coordinates to test
        - length (int/float): side length of cube

    Returns:
        - (bool): True iff coordinates are at the center of any of the 6
                  faces of a `length`^3 cube

    Raises:
        - ValueError if the passed coordinates does not have exactly 3 values.
    """
    if len(coordinates) != 3:
        raise ValueError('coordinates must be a 3-element tuple.')

    # By definition, coordinates must not be a corner or the center of the cube
    return not (is_corner(coordinates, length) or
                is_cell_center(coordinates, length))
