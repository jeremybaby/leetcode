/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/* Solution: 进位设置carryBit */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode *head, *curr, *node;
    curr = (struct ListNode *)malloc(sizeof(struct ListNode));
    head = curr;
    int sum = 0;
    int carrybit = 0;

    while (l1 || l2) {
        sum = 0;
        node = (struct ListNode *)malloc(sizeof(struct ListNode));
        if (l1) {
           sum += l1->val; 
           l1 = l1->next;
        }
        if (l2) {
            sum += l2->val;
            l2 = l2->next;
        }
        sum += carrybit;
        node->val = sum % 10;
        carrybit = sum >= 10 ? 1 : 0;
        curr->next = node;
        curr = curr->next;
    }
    if (carrybit) {
        node = (struct ListNode*)malloc(sizeof(struct ListNode));
        node->val = 1;
        node->next = NULL;
        curr->next = node;
    } else {
        curr->next = NULL;
    }
    return head->next;
}

/* Promote1: 不使用进位，只对sum进行处理 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode *head, *curr, *node; 
    curr = (struct ListNode *)malloc(sizeof(struct ListNode));
    head = curr;
    int sum = 0;

    while (l1 || l2) {
        node = (struct ListNode*)malloc(sizeof(struct ListNode));
        if (l1) {
            sum += l1->val;
            l1 = l1->next;
        }
        if (l2) {
            sum += l2->val;
            l2 = l2->next;
        }
        node->val = sum % 10;
        /* 注意此处的sum如何处理进位 */
        sum /= 10;
        curr->next = node;
        curr = curr->next;
    }
    /* 遍历完还有进位的情况 */
    if (sum) {
        node = (struct ListNode*)malloc(sizeof(struct ListNode));
        node->val = 1;
        node->next = NULL;
        curr->next = node;
    } else {
        curr->next = NULL;
    }

    return head->next;
}

/* Promote2: 将遍历完还存在进位的情况一起处理 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode *head, *curr, *node; 
    curr = (struct ListNode *)malloc(sizeof(struct ListNode));
    head = curr;
    int sum = 0;

    while (l1 || l2 || sum) {
        node = (struct ListNode*)malloc(sizeof(struct ListNode));
        if (l1) {
            sum += l1->val;
            l1 = l1->next;
        }
        if (l2) {
            sum += l2->val;
            l2 = l2->next;
        }
        node->val = sum % 10;
        /* 注意此处的sum如何处理进位 */
        sum /= 10;
        curr->next = node;
        curr = curr->next;
    }
    /* 遍历完还有进位的情况 */
    curr->next = NULL;

    return head->next;
}





