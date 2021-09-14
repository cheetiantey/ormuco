import java.util.*;

public class LRUCache {
    HashMap<Integer, ListNode> hashtable = new HashMap<Integer, ListNode>();
    ListNode head;
    ListNode tail;

    int totalItemsInCache;
    int maxCapacity;

    public LRUCache (int maxCapacity) {
    // Cache starts empty and capacity is set by client
    totalItemsInCache = 0;
    this.maxCapacity = maxCapacity;

    // Dummy head and tail nodes to avoid empty states
    head = new ListNode();
    tail = new ListNode();

    // Wire the head and tail together
    head.next = tail;
    tail.prev = head;
    }

    public Integer get (int key) {
    ListNode node = hashtable.get(key);

    if (node == null) {
        return null;
    }

    // Item has been accessed, move to the front of the cache
    moveToFront(node);

    return node.value;
    }

    public void put (int key, int value) {
    ListNode node = hashtable.get(key);
    
    // Add the item if the item isn't already in the cache
    if (node == null) {
        ListNode newNode = new ListNode();
        newNode.key = key;
        newNode.value = value;

        // Add to the key to a hashtable and the value to a list
        hashtable.put(key, newNode);
        addToFront(newNode);
        totalItemsInCache++;

        // If we've exceeded the capacity of the cache, remove the 
        // Least recently used item
        if (totalItemsInCache > maxCapacity) {
        removeLRUEntry();
        }
    } else {
        // If the item is in the cache, move it to the front of the cache
        node.value = value;
        moveToFront(node);
    }
    }

    // Remove an entry from the cache
    private void removeLRUEntry() {
        ListNode tailItem = tail.prev;
        removeFromList(tail.prev);

        hashtable.remove(tailItem.key);
        totalItemsInCache--;
    }


    // Add a new item to the front of the cache
    private void addToFront(ListNode node) {
        node.prev = head;
        node.next = head.next;

        head.next.prev = node;
        head.next = node;
    }

    // Remove an item from the cache
    private void removeFromList (ListNode node) {
        ListNode savedPrev = node.prev;
        ListNode savedNext = node.next;

        savedPrev.next = savedNext;
        savedNext.prev = savedPrev;
    }

    // Move the item that we've just "touched" to the front
    private void moveToFront (ListNode node) {
        removeFromList(node);
        addToFront(node);
    }

    private class ListNode {
        int key;
        int value;

        ListNode prev;
        ListNode next;
    }

    public static void main (String args[]) {
        
        // Set up a LRU Cahce of size 3
        // Add 4 items into the cache
        LRUCache lru = new LRUCache(3);
        System.out.println("Adding 4 items to the cache of size 3...");
        lru.put(1, 100);
        lru.put(2, 200);
        lru.put(3, 300);
        lru.put(4, 400);
        System.out.println("Trying to get the first item being put in...(Should be null): " + lru.get(1));
        System.out.println("Trying to get the value of key '2'...(Should be 200): " + lru.get(2));
    }
}

  