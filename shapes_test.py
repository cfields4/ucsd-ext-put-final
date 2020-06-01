import unittest
from shapes import Point, Circle


# Helper functions - use these for data verification when appropriate.
def point_data(point):
    """Return tuple of Point data for comparison."""
    return point.x, point.y


def circle_data(circle):
    """Return tuple of Circle data for comparison."""
    return (
        (circle.center.x, circle.center.y),
        circle.radius
        )


class PointTests(unittest.TestCase):

    def test_create_point_no_data(self):
        """P-1. Create a Point with no arguments."""
        # Create a tuple of what the answer from point_data should be
        expected = (0, 0)
        point = Point()
        self.assertEqual(point_data(point), expected)

    def test_create_point_with_data(self):
        """P-2. Create a Point with values."""
        expected = (2, 3)
        point = Point(2, 3)
        self.assertEqual(point_data(point), expected)

    def test_point_modification(self):
        """P-3. Verify modification of x, y works."""
        expected = (-1, 5)
        point = Point()
        point.x, point.y = -1, 5
        self.assertEqual(point_data(point), expected)

    def test_point_iterable(self):
        """P-4. Verify Point is iterable."""
        expected = (2, 3)
        point = Point(2, 3)
        x, y = point
        self.assertEqual((x, y), expected)
        j, k = point
        self.assertEqual((j, k), expected)

    def test_point_not_iterator(self):
        """P-4a. Verify point is not an iterator"""
        point = Point(2, 3)
        x = iter(point)
        self.assertIs(x == point, False)
        with self.assertRaises(TypeError):
            next(point)

    def test_magnitude(self):
        """P-5. Verify Point magnitude property."""
        expected = 3.605551275463989
        point = Point(2, 3)
        self.assertEqual(point.magnitude, expected)

    def test_magnitude_changes(self):
        """P-6. Verify magnitude property changes after Point changed."""
        expected = 5
        point = Point(-1, 6)
        point.x, point.y = 3, 4
        self.assertEqual(point.magnitude, expected)

    def test_distance(self):
        """P-7. Verify distance between two Point objects."""
        expected = 5
        point1 = Point(2, 3)
        point2 = Point(5, 7)
        self.assertEqual(point1.distance(point2), expected)

    def test_point_addition(self):
        """P-8. Verify Point addition."""
        expected1 = (2, 3)
        expected2 = (4, 5)
        expected3 = (6, 8)
        point1 = Point(2, 3)
        point2 = Point(4, 5)
        point3 = point1 + point2
        # Ensure original points unchanged
        self.assertEqual(point_data(point1), expected1)
        self.assertEqual(point_data(point2), expected2)
        # Verify new point is correct
        self.assertEqual(point_data(point3), expected3)

    def test_point_plus_equal_addition(self):
        """P-8a. Verify Point += mutating addition."""
        expected = (6, 8)
        point1 = Point(2, 3)
        # Save the id to make sure it doesn't change.
        id1 = id(point1)
        point2 = Point(4, 5)
        # Add using +=
        point1 += point2
        self.assertEqual(point_data(point1), expected)
        # Verify point2 has not changed
        expected = (4, 5)
        self.assertEqual(point_data(point2), expected)
        # Verify that point1 is the same object
        self.assertEqual(id(point1), id1)

    def test_point_str(self):
        """P-9. Verify Point str result."""
        expected = "Point at (2, 3)"
        point = Point(2, 3)
        self.assertEqual(str(point), expected)

    def test_point_repr(self):
        """P-10. Verify Point repr result."""
        expected = "Point(x=2, y=3)"
        point = Point(2, 3)
        self.assertEqual(repr(point), expected)

    # Remaining Point tests go here

    def test_create_point_from_tuple(self):
        """P-11. Create a Point using from_tuple."""
        expected = "Point(x=2, y=3)"
        point = Point(2, 3)
        self.assertEqual(repr(Point.from_tuple(point)), expected)

    def test_error_point_from_tuple_no_args(self):
        """P-12. Verify error when using from_tuple with no arguments"""
        with self.assertRaises(TypeError) as append:
            Point.from_tuple()
        self.assertEqual("from_tuple() missing 1 required positional argument: 'coords'", str(append.exception))

    def test_point_mod_loc_from_tuple(self):
        """P-13. Verify mod of x, y using loc_from_tuple."""
        expected = Point(5, 6)
        point1 = Point(3, 4)
        point2 = point1.loc_from_tuple((5, 6))
        self.assertEqual(point2, expected)

    def test_point_mod_loc_from_tuple_no_args(self):
        """P-14. Verify error when using loc_from_tuple with no arguments."""
        expected = Point(0, 0)
        point = Point(3, 4)
        self.assertEqual(point.loc_from_tuple(), expected)

    def test_scalar_mult_right(self):
        """P-15. Verify Point multiplied with scalar."""
        expected = (6, 9)
        point1 = Point(2, 3)
        point3 = point1 * 3
        self.assertEqual(point_data(point3), expected)

    def test_scalar_mult_left(self):
        """P-16. Verify scalar multiplied with Point."""
        expected = (6, 9)
        point1 = Point(2, 3)
        point3 = 3 * point1
        self.assertEqual(point_data(point3), expected)

    def test_scalar_mult_plus_equal(self):
        """P-17. Verify Point *= mutating multiply with scalar."""
        expected = False
        point1 = Point(2, 3)
        id1 = id(point1)
        point1 *= 4
        self.assertEqual((id1 == id(point1)), expected)


class CircleTests(unittest.TestCase):

    def test_circle_point_objects_different(self):
        """C-0. Make sure Circle centers are different objects for default."""
        # In other words, they should have the same VALUES,
        # But NOT be the same objects.
        circle1 = Circle()
        circle2 = Circle()
        self.assertIsNot(circle1.center, circle2.center)
        self.assertEqual(circle_data(circle1), circle_data(circle2))

    def test_create_no_input(self):
        """C-1. Create Circle with no arguments."""
        # Create a tuple of what the answer from circle_data should be
        expected = ((0, 0), 1)
        circle = Circle()
        self.assertEqual(circle_data(circle), expected)

    def test_create_only_point_input(self):
        """C-2. Create Circle with Point but no radius."""
        expected = ((2, 3), 1)
        circle = Circle(center=Point(2, 3))
        self.assertEqual(circle_data(circle), expected)
        # Also make sure the circle's center is the same as the point input.
        point = Point(2, 3)
        point_id = id(point)
        circle = Circle(center=point)
        self.assertEqual(circle_data(circle), expected)
        self.assertEqual(point_id, id(circle.center))

    def test_create_only_radius_input(self):
        """C-3. Create Circle with radius but no Point."""
        expected = ((0, 0), 2.5)
        circle = Circle(radius=2.5)
        self.assertEqual(circle_data(circle), expected)
        # Make sure radius=0 works (edge case of Circles)
        expected = ((0, 0), 0)
        circle = Circle(radius=0)
        self.assertEqual(circle_data(circle), expected)

    def test_create_point_and_radius_input(self):
        """C-4. Create Circle with Point and radius."""
        expected = ((2, 3), 1.5)
        circle = Circle(center=Point(2, 3), radius=1.5)
        self.assertEqual(circle_data(circle), expected)

    def test_create_no_keywords(self):
        """C-5. Create Circle without keywords."""
        expected = ((2, 3), 1.5)
        circle = Circle(Point(2, 3), 1.5)
        self.assertEqual(circle_data(circle), expected)

    def test_move_center(self):
        """C-5A. Verify moving center Point of Circle works."""
        expected = ((6, 2), 1.5)
        point = Point(2, 3)
        circle = Circle(point, 1.5)
        point.x = 6
        point.y = 2
        self.assertEqual(circle_data(circle), expected)

    def test_area(self):
        """C-6. Verify area property."""
        expected = 12.566370614359172
        circle = Circle(radius=2)
        self.assertIsNot(circle.area, expected)

    # Remaining Circle tests go here

    def test_change_radius(self):
        """C-7. Verify radius attribute change works."""
        expected = 2
        point1 = Point(2, 3)
        circle1 = Circle(center=point1, radius=4)
        circle1.radius = 2
        self.assertEqual(circle1.radius, expected)

    def test_area_changed(self):
        """C-8. Verify area changes correctly when radius changes."""
        expected = 1
        circle1 = Circle(Point(1, 2), 4)
        circle1.radius = 1
        self.assertEqual(circle1.area, expected)

    def test_change_center(self):
        """C-9. Verify center attribute change works."""
        expected = (2, 3)
        circle = Circle(Point(3, 4), 4)
        center = circle.center
        center.x = 2
        center.y = 3
        self.assertEqual(point_data(circle.center), expected)

    def test_illegal_center_creation(self):
        """C-10. Verify error if center is not a Point on creation."""
        with self.assertRaises(TypeError):
            circle = Circle(center=(0, 0), radius=1.5)

    def test_illegal_center_modification(self):
        """C-11. Verify error if changing center to something not a Point."""
        with self.assertRaises(TypeError):
            circle = Circle(center=(0, 0), radius=1.5)

    def test_diameter(self):
        """C-12. Verify diameter property works."""
        expected = 4
        circle = Circle(Point(1, 2), 2)
        self.assertEqual(circle.diameter, expected)

    def test_diameter_changes(self):
        """C-13. Verify diameter changes works."""
        expected = 4
        circle = Circle(Point(1, 2), 4)
        circle.radius = 2
        self.assertEqual(circle.diameter, expected)

    def test_create_negative_radius(self):
        """C-14. Verify error when radius < 0."""
        with self.assertRaises(ValueError):
            circle = Circle(Point(1, 2), -1)

    def test_change_negative_radius(self):
        """C-15. Verify error when radius < 0."""
        with self.assertRaises(ValueError):
            circle = Circle(Point(1, 2), 2)
            circle.radius = -1

    def test_change_negative_diameter(self):
        """C-16. Verify error when diameter < 0."""
        with self.assertRaises(ValueError):
            circle = Circle(Point(1, 2), 2)
            circle.diameter = -1

    def test_circle_addition(self):
        """C-17. Verify Circle addition."""
        expected = 'Circle(center=Point(3, 4), radius=3.5)'
        circle1 = Circle(radius=2.5, center=Point(1, 1))
        circle2 = Circle(center=Point(2, 3), radius=1)
        circle3 = circle1 + circle2
        self.assertEqual(circle3, expected)

    def test_circle_plus_equal_addition(self):
        """C-17a. Verify Circle += mutating addition."""
        expected = 'Circle(center=Point(3, 4), radius=3.5)'
        circle1 = Circle(radius=2.5, center=Point(1, 1))
        circle2 = Circle(center=Point(2, 3), radius=1)
        circle1 += circle2
        self.assertEqual(circle1, expected)

    def test_circle_str(self):
        """C-18. Verify Circle str result."""
        expected = 'Circle with center at (1, 2) and radius 2'
        point1 = Point(1, 2)
        circle = Circle(center=point1, radius=2)
        self.assertEqual(str(circle), expected)

    def test_circle_repr(self):
        """C-19. Verify Circle repr result."""
        expected = 'Circle(center=Point(1, 2), radius=2)'
        point1 = Point(1, 2)
        circle = Circle(center=point1, radius=2)
        self.assertEqual(repr(circle), expected)

    def test_circle_create_from_tuple(self):
        """C-20. Test circle creation using from_tuple."""
        expected = ((3, 4), 3)
        center_point = 3, 4
        circle = Circle.from_tuple(center_point, 3)
        self.assertEqual(circle_data(circle), expected)

    def test_circle_create_from_tuple_no_args(self):
        """C-21. Verify error using Circle.from_tuple with no arguments."""
        with self.assertRaises(TypeError):
            circle = Circle.from_tuple()

    def test_circle_create_from_tuple_only_tuple(self):
        """C-22. Test circle creation using from_tuple with only tuple."""
        expected = 'Circle(center=Point(3, 4), radius=1)'
        center_point = 3, 4
        circle = Circle.from_tuple(center=center_point)
        self.assertEqual(circle, expected)

    def test_circle_modify_center_from_tuple(self):
        """C-23. Test circle modify with center_from_tuple method."""
        expected = (4, 5)
        circle = Circle(Point(2, 3), 2)
        new_center = 4, 5
        self.assertEqual(point_data(circle.center_from_tuple(new_center)), expected)

    def test_circle_modify_center_from_tuple_no_args(self):
        """C-24. Verify error using center_from_tuple with no arguments."""
        with self.assertRaises(TypeError):
            circle = Circle.from_tuple()


if __name__ == "__main__":
    unittest.main()
