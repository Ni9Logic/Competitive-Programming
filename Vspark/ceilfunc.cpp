#include <bits/stdc++.h>
using namespace std;

struct Tree
{
    Tree *left, *right;
    int data;
    Tree()
    {
        left = right = NULL;
    }
    Tree *createNode(int dat)
    {
        Tree *n = new Tree();
        n->data = dat;

        return n;
    }
    Tree *insert(Tree *root, int dat)
    {
        if (root == NULL)
        {
            root = createNode(dat);
            return root;
        }
        if (dat > root->data)
            root->right = insert(root->right, dat);
        else
            root->left = insert(root->left, dat);

        return root;
    }
    void display(Tree *root)
    {
        if (root == NULL)
            return;

        display(root->left);
        cout << root->data << " ";
        display(root->right);
    }
    int countLeftChild(Tree *r)
    {
        if (r == NULL)
            return 0;
        if (r->left == NULL)
            // NO Left child.
            return countLeftChild(r->left);
        else
            // Left child present.
            return countLeftChild(r->right) + countLeftChild(r->left) + 1;
    }
    int countRightChild(Tree *r)
    {
        if (r == NULL)
            return 0;
        if (r->right == NULL)
            // NO Left child.
            return countRightChild(r->right);
        else
            // Left child present.
            return countRightChild(r->right) + countRightChild(r->left) + 1;
    }
};

int main()
{
    int count = 0;
    vector<Tree *> children;
    int n, nums;
    cin >> n >> nums;
    while (n--)
    {
        Tree *root = NULL;
        vector<int> num(nums);
        for (int i = 0; i < nums; i++)
        {
            int data;
            cin >> data;
            root = root->insert(root, data);
        }
        children.push_back(root);
    }

    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
        {
            //! Left and Right children count of both trees!
            int child1left = children[i]->countLeftChild(children[i]);
            int child1right = children[i]->countRightChild(children[i]);
            int child2left = children[j]->countLeftChild(children[j]);
            int child2right = children[j]->countRightChild(children[j]);

            if (child1left == child2left and child2right == child1right)
                count++;
            if (child1left == child2left and child1right == 0 and child2right == 0)
                count++;
            if (child2right == child1right and child1left == 0 and child2left == 0)
                count++;
            if (child1right == child2left)
                count++;
        }

    cout << count << endl;
}