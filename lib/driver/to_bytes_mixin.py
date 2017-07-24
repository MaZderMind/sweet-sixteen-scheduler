import logging

log = logging.getLogger("ToBytesMixin")


def batch(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]


def segment_8_tuple_to_byte(segment_8_tuple):
    return \
        (0x1 << 0) * (1 if segment_8_tuple[0] else 0) + \
        (0x1 << 1) * (1 if segment_8_tuple[1] else 0) + \
        (0x1 << 2) * (1 if segment_8_tuple[2] else 0) + \
        (0x1 << 3) * (1 if segment_8_tuple[3] else 0) + \
        (0x1 << 4) * (1 if segment_8_tuple[4] else 0) + \
        (0x1 << 5) * (1 if segment_8_tuple[5] else 0) + \
        (0x1 << 6) * (1 if segment_8_tuple[6] else 0) + \
        (0x1 << 7) * (1 if segment_8_tuple[7] else 0)


class ToBytesMixin(object):
    def to_bytes(self):
        """
        Convert a Frame to a Bytes-Object with each segment being one bit

        :type self: lib.frame.Frame
        :return: lib.frame.Frame
        """
        byte_array = []
        for segment_8_tuple in batch(self.segments, 8):
            byte = segment_8_tuple_to_byte(segment_8_tuple)
            byte_array.append(byte)

        log.debug("frame-segments {} converted to bytes {}"
                  .format(self.segments, byte_array))

        return bytes(byte_array)
