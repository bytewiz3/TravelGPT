import time 
import logging 
 
# 64-bit ID division 
WORKER_ID_BITS = 5 
DATACENTER_ID_BITS = 5 
SEQUENCE_BITS = 12 
 
# Maximum value calculation 
MAX_WORKER_ID = -1 ^ (-1 << WORKER_ID_BITS)  # 2**5-1 0b11111 
MAX_DATACENTER_ID = -1 ^ (-1 << DATACENTER_ID_BITS) 
 
# Shift offset calculation 
WOKER_ID_SHIFT = SEQUENCE_BITS 
DATACENTER_ID_SHIFT = SEQUENCE_BITS + WORKER_ID_BITS 
TIMESTAMP_LEFT_SHIFT = SEQUENCE_BITS + WORKER_ID_BITS + DATACENTER_ID_BITS 
 
# Sequence cycle mask 
SEQUENCE_MASK = -1 ^ (-1 << SEQUENCE_BITS) 
 
# Twitter epoch timestamp 
TWEPOCH = 1288834974657 
 
logger = logging.getLogger('flask.app') 
 
 
class IdWorker(object): 
    """ 
    Used to generate IDs 
    """ 
 
    def __init__(self, datacenter_id, worker_id, sequence=0): 
        """ 
        Initialization 
        :param datacenter_id: Datacenter (machine area) ID 
        :param worker_id: Worker ID (machine ID) 
        :param sequence: Starting sequence number 
        """ 
        # sanity check 
        if worker_id > MAX_WORKER_ID or worker_id < 0: 
            raise ValueError('worker_id is out of bounds') 
 
        if datacenter_id > MAX_DATACENTER_ID or datacenter_id < 0: 
            raise ValueError('datacenter_id is out of bounds') 
 
        self.worker_id = worker_id 
        self.datacenter_id = datacenter_id 
        self.sequence = sequence 
 
        self.last_timestamp = -1  # Last calculated timestamp 
 
    def _gen_timestamp(self): 
        """ 
        Generate integer timestamp 
        :return:int timestamp 
        """ 
        return int(time.time() * 1000) 
 
    def get_id(self): 
        """ 
        Get a new ID 
        :return: 
        """ 
        timestamp = self._gen_timestamp() 
 
        # Clock drift 
        if timestamp < self.last_timestamp: 
            logging.error('clock is moving backwards. Rejecting requests until {}'.format(self.last_timestamp)) 
            raise 
 
        if timestamp == self.last_timestamp: 
            self.sequence = (self.sequence + 1) & SEQUENCE_MASK 
            if self.sequence == 0: 
                timestamp = self._til_next_millis(self.last_timestamp) 
        else: 
            self.sequence = 0 
 
        self.last_timestamp = timestamp 
 
        new_id = ((timestamp - TWEPOCH) << TIMESTAMP_LEFT_SHIFT) | (self.datacenter_id << DATACENTER_ID_SHIFT) | \ 
                 (self.worker_id << WOKER_ID_SHIFT) | self.sequence 
        return new_id 
 
    def _til_next_millis(self, last_timestamp): 
        """ 
        Wait until next millisecond 
        """ 
        timestamp = self._gen_timestamp() 
        while timestamp <= last_timestamp: 
            timestamp = self._gen_timestamp() 
        return timestamp 
 
 
DefaultIdWorker = IdWorker(1, 2, 0) 
 
if __name__ == '__main__': 
    print(DefaultIdWorker.get_id()) 
